#! /usr/bin/env python3

import argparse
import cmd
import configparser
import csv
import glob
import json
import os
import pathlib
import re
import shlex
import sys
import textwrap
import time
from functools import wraps

from senzing import (
    SzConfig,
    SzConfigManager,
    SzDiagnostic,
    SzEngine,
    SzEngineFlags,
    SzError,
    SzProduct,
)

# TODO Add back in when consolidated modules into a helper module
# import G2Paths
# from G2IniParams import G2IniParams
# from senzing import szconfig, szconfigmanager, szdiagnostic, szengine, szproduct
# from senzing.szengineflags import SzEngineFlags
# from senzing.szerror import SzError


try:
    import atexit
    import readline

    readline_avail = True
except ImportError:
    readline_avail = False

try:
    import pyperclip

    pyperclip_avail = True
except ImportError:
    pyperclip_avail = False

try:
    import orjson

    orjson_avail = True
except ImportError:
    orjson_avail = False


class Colors:
    @classmethod
    def apply(cls, in_string, color_list=None):
        """Apply list of colors to a string"""
        if color_list:
            prefix = "".join(
                [getattr(cls, i.strip().upper()) for i in color_list.split(",")]
            )
            suffix = cls.RESET
            return f"{prefix}{in_string}{suffix}"
        return in_string

    @classmethod
    def set_theme(cls, theme):
        if theme.upper() == "DEFAULT":
            cls.GOOD = cls.FG_GREEN
            cls.BAD = cls.FG_RED
            cls.CAUTION = cls.FG_YELLOW
            cls.HIGHLIGHT1 = cls.FG_MAGENTA
            cls.HIGHLIGHT2 = cls.FG_BLUE
        elif theme.upper() == "LIGHT":
            cls.GOOD = cls.FG_LIGHTGREEN
            cls.BAD = cls.FG_LIGHTRED
            cls.CAUTION = cls.FG_LIGHTYELLOW
            cls.HIGHLIGHT1 = cls.FG_LIGHTMAGENTA
            cls.HIGHLIGHT2 = cls.FG_LIGHTBLUE

    # styles
    RESET = "\033[0m"
    BOLD = "\033[01m"
    DIM = "\033[02m"
    ITALICS = "\033[03m"

    UNDERLINE = "\033[04m"
    BLINK = "\033[05m"
    REVERSE = "\033[07m"
    STRIKETHROUGH = "\033[09m"
    INVISIBLE = "\033[08m"
    # foregrounds
    FG_BLACK = "\033[30m"
    FG_WHITE = "\033[97m"
    FG_BLUE = "\033[34m"
    FG_MAGENTA = "\033[35m"
    FG_CYAN = "\033[36m"
    FG_YELLOW = "\033[33m"
    FG_GREEN = "\033[32m"
    FG_RED = "\033[31m"
    FG_LIGHTBLACK = "\033[90m"
    FG_LIGHTWHITE = "\033[37m"
    FG_LIGHTBLUE = "\033[94m"
    FG_LIGHTMAGENTA = "\033[95m"
    FG_LIGHTCYAN = "\033[96m"
    FG_LIGHTYELLOW = "\033[93m"
    FG_LIGHTGREEN = "\033[92m"
    FG_LIGHTRED = "\033[91m"


# Override argparse error to format message
class SzCommandArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        # self.print_help(sys.stderr)
        self.exit(2, colorize_msg(f"\nERROR: {self.prog} - {message}\n", "error"))


def cmd_decorator(cmd_has_args=True):
    """Decorator for do_* commands to parse args, display help, set response variables etc."""

    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            cmd_args = args[0]

            # Check if command has modifiers for JSON and color formatting
            valid_modifiers = [
                "json",
                "jsonl",
                "color",
                "colour",
                "nocolor",
                "nocolour",
            ]

            # Capture end of args to detect the valid_modifiers
            cmd_modifiers = cmd_args[-13:].split(" ")
            cmd_modifiers.reverse()

            for modifier in (
                modifier
                for modifier in cmd_modifiers
                if modifier.lower() in valid_modifiers
            ):
                if modifier.lower() in ["json", "jsonl"]:
                    self.json_output_format = modifier.lower()
                if modifier.lower() in ["color", "colour"]:
                    self.json_output_color = True
                if modifier.lower() in ["nocolor", "nocolour"]:
                    self.json_output_color = False

                # Don't remove modifiers if we are setting formatting options
                if func.__name__ not in ["do_setOutputFormat", "do_setOutputColor"]:
                    cmd_args = cmd_args.rstrip(modifier).rstrip()

            if cmd_has_args:
                try:
                    # Parse args for a command
                    kwargs["parsed_args"] = self.parser.parse_args(
                        [f"{func.__name__[3:]}"] + self.parse(cmd_args)
                    )

                    # Create a dict with a key of "flags" to unpack in calling
                    # methods for flag argument in szengine methods
                    if hasattr(kwargs["parsed_args"], "flags"):
                        kwargs["flags_dict"] = (
                            {"flags": get_engine_flags(kwargs["parsed_args"].flags)}
                            if kwargs["parsed_args"].flags
                            else {}
                        )

                # Catch argument errors from parser and display the commands help
                except SystemExit:
                    self.do_help(func.__name__)
                    return
                # Catch parsing errors such as missing single quote around JSON etc.
                # Error is displayed in parse()
                except ValueError:
                    return
                except KeyError as err:
                    self.print_error(err)
                    return

            # Run the decorated function passing back args
            try:
                if self.timer_on:
                    timer_start = time.perf_counter()
                func(self, **kwargs)
                if self.timer_on:
                    execTime = time.perf_counter() - timer_start
                    # Don't use printResponse for this, don't want this message as the last response
                    print(
                        colorize_msg(
                            f"\nApproximate execution time (s): {execTime:.5f}\n",
                            "info",
                        )
                    )
            except (SzError, IOError) as err:
                self.print_error(err)

        return wrapper

    return decorator


class SzCmdShell(cmd.Cmd, object):
    def __init__(self, engine_settings, debug, hist_disable):
        cmd.Cmd.__init__(self)

        Colors.set_theme("DEFAULT")

        try:
            # TODO What else needs verbose_logging?
            self.sz_engine = SzEngine(
                # TODO Change instance name in all tools
                "pySzEngine",
                engine_settings,
                verbose_logging=debug_trace,
            )
            self.sz_product = SzProduct("pySzProduct", engine_settings, debug_trace)
            self.sz_diagnostic = SzDiagnostic(
                "pySzDiagnostic", engine_settings, verbose_logging=debug_trace
            )
            self.sz_config = SzConfig(
                "pySzConfig", engine_settings, verbose_logging=debug_trace
            )
            self.sz_configmgr = SzConfigManager(
                "pySzConfigmgr", engine_settings, verbose_logging=debug_trace
            )
        # Change all ex to err
        except SzError as ex:
            self.print_error(ex)
            self.postloop()
            sys.exit(1)

        # Hide methods - could be deprecated, undocumented, not supported, experimental
        self.__hidden_methods = (
            "do_EOF",
            "do_findInterestingEntitiesByEntityID",
            "do_findInterestingEntitiesByRecordID",
            "do_getRedoRecord",
            "do_getFeature",
            "do_help",
            "do_hidden",
            "do_shell",
        )

        # Get engine flags for use in auto completion
        self.engine_flags_list = list(SzEngineFlags.__members__.keys())

        self.intro = ""
        self.prompt = "(szcmd) "

        self.initialized = self.restart = self.restart_debug = self.quit = (
            self.timer_on
        ) = False
        self.debug_trace = debug
        self.timer_start = self.timer_end = None
        self.last_response = ""

        # Readline and history
        self.hist_avail = False
        self.hist_disable = hist_disable
        self.hist_file_name = self.histFileError = None
        self.hist_check()

        # Setup for pretty printing
        self.json_output_color = True
        self.json_output_format = "json"

        # Only display can't read/write config message once, not at all in container
        self.config_error = 0
        env_launched = os.getenv("SENZING_DOCKER_LAUNCHED", None)
        self.docker_launched = (
            True if env_launched in ("y", "yes", "t", "true", "on", "1") else False
        )

        # Check if there is a config file and use config
        if not self.docker_launched:
            path = pathlib.Path(sys.argv[0])
            config_file = f"~/.{path.stem.lower()}{'.ini'}"
            self.config_file = pathlib.Path(config_file).expanduser()
            config_exists = pathlib.Path(self.config_file).exists()
            self.config = configparser.ConfigParser()

            if config_exists:
                try:
                    with open(self.config_file, "r") as _:
                        pass
                    self.config.read(self.config_file)
                    self.json_output_format = self.config["FORMATTING"]["JsonFormat"]
                    self.json_output_color = self.config["FORMATTING"].getboolean(
                        "ColorOutput"
                    )
                except IOError as ex:
                    self.print_response(
                        colorize_msg(
                            "Error reading the config file, saved"
                            f" config has not been applied: {ex}"
                        ),
                        "warning",
                    )
                except (configparser.Error, KeyError) as ex:
                    self.print_response(
                        colorize_msg(
                            "Error reading entries from the config file, saved config"
                            f" has not been applied: {ex}"
                        ),
                        "warning",
                    )
            else:
                # If a configuration file doesn't exist attempt to create one
                if not self.docker_launched:
                    self.write_config()

        # do_* command parsers

        self.parser = SzCommandArgumentParser(
            add_help=False, prog="szcommand", usage=argparse.SUPPRESS
        )
        self.subparsers = self.parser.add_subparsers()

        # szconfig parsers

        getConfig_parser = self.subparsers.add_parser(
            "getConfig", usage=argparse.SUPPRESS
        )
        getConfig_parser.add_argument("config_id", type=int)

        # szconfigmanager parsers

        replaceDefaultConfigID_parser = self.subparsers.add_parser(
            "replaceDefaultConfigID", usage=argparse.SUPPRESS
        )
        replaceDefaultConfigID_parser.add_argument(
            "current_default_config_id", type=int
        )
        replaceDefaultConfigID_parser.add_argument("new_default_config_id", type=int)

        setDefaultConfigID_parser = self.subparsers.add_parser(
            "setDefaultConfigID", usage=argparse.SUPPRESS
        )
        setDefaultConfigID_parser.add_argument("config_id", type=int)

        # szdiagnostic parsers

        checkDatastorePerformance_parser = self.subparsers.add_parser(
            "checkDatastorePerformance", usage=argparse.SUPPRESS
        )
        checkDatastorePerformance_parser.add_argument(
            "secondsToRun", default=3, nargs="?", type=int
        )

        getFeature_parser = self.subparsers.add_parser(
            "getFeature", usage=argparse.SUPPRESS
        )
        getFeature_parser.add_argument("featureID", nargs="?", type=int)

        purgeRepository_parser = self.subparsers.add_parser(
            "purgeRepository", usage=argparse.SUPPRESS
        )
        purgeRepository_parser.add_argument(
            "-FORCEPURGE",
            "--FORCEPURGE",
            action="store_true",
            default=False,
            dest="force_purge",
            required=False,
        )

        # szengine parsers

        addRecord_parser = self.subparsers.add_parser(
            "addRecord", usage=argparse.SUPPRESS
        )
        addRecord_parser.add_argument("data_source_code")
        addRecord_parser.add_argument("record_id")
        addRecord_parser.add_argument("record_definition")
        addRecord_parser.add_argument("-f", "--flags", nargs="+", required=False)

        deleteRecord_parser = self.subparsers.add_parser(
            "deleteRecord", usage=argparse.SUPPRESS
        )
        deleteRecord_parser.add_argument("data_source_code")
        deleteRecord_parser.add_argument("record_id")
        deleteRecord_parser.add_argument("-f", "--flags", nargs="+", required=False)

        exportCSVEntityReport_parser = self.subparsers.add_parser(
            "exportCSVEntityReport", usage=argparse.SUPPRESS
        )
        exportCSVEntityReport_parser.add_argument("output_file")
        exportCSVEntityReport_parser.add_argument(
            "-f", "--flags", nargs="+", required=False
        )
        exportCSVEntityReport_parser.add_argument(
            "-t", "--csv_column_list", required=False, type=str
        )

        exportJSONEntityReport_parser = self.subparsers.add_parser(
            "exportJSONEntityReport", usage=argparse.SUPPRESS
        )
        exportJSONEntityReport_parser.add_argument("output_file")
        exportJSONEntityReport_parser.add_argument(
            "-f", "--flags", nargs="+", required=False
        )

        findInterestingEntitiesByEntityID_parser = self.subparsers.add_parser(
            "findInterestingEntitiesByEntityID", usage=argparse.SUPPRESS
        )
        findInterestingEntitiesByEntityID_parser.add_argument("entity_id", type=int)
        findInterestingEntitiesByEntityID_parser.add_argument(
            "-f", "--flags", nargs="+", required=False
        )

        findInterestingEntitiesByRecordID_parser = self.subparsers.add_parser(
            "findInterestingEntitiesByRecordID", usage=argparse.SUPPRESS
        )
        findInterestingEntitiesByRecordID_parser.add_argument("data_source_code")
        findInterestingEntitiesByRecordID_parser.add_argument("record_id")
        findInterestingEntitiesByRecordID_parser.add_argument(
            "-f", "--flags", nargs="+", required=False
        )

        # TODO
        # TODO What if a char or non-int is sent?
        def list_of_ints(ints):
            print(list(map(int, ints.split(","))))
            # TODO Comprehension faster?
            return list(map(int, ints.split(",")))

        # TODO Add required False to all parsers
        findNetworkByEntityID_parser = self.subparsers.add_parser(
            "findNetworkByEntityID", usage=argparse.SUPPRESS
        )
        # findNetworkByEntityID_parser.add_argument("entity_list")
        findNetworkByEntityID_parser.add_argument("entity_list", type=list_of_ints)
        findNetworkByEntityID_parser.add_argument("max_degrees", type=int)
        findNetworkByEntityID_parser.add_argument("build_out_degree", type=int)
        findNetworkByEntityID_parser.add_argument("max_entities", type=int)
        findNetworkByEntityID_parser.add_argument(
            "-f", "--flags", nargs="+", required=False
        )

        # TODO
        def list_of_tuples(rec_keys: str) -> list[tuple[str, str]]:

            error_msg = "error parsing, expecting: 'DATA_SOURCE:RECORD_ID, DATA_SOURCE:RECORD_ID, ...'"

            if "," not in rec_keys or ":" not in rec_keys:
                raise argparse.ArgumentTypeError(error_msg)

            try:
                rec_keys_list = [
                    (values[0].strip(), values[1].strip())
                    for values in (aset.split(":") for aset in rec_keys.split(","))
                ]
                print(rec_keys_list)
            except IndexError as err:
                raise argparse.ArgumentTypeError(error_msg) from err

            return rec_keys_list

        findNetworkByRecordID_parser = self.subparsers.add_parser(
            "findNetworkByRecordID", usage=argparse.SUPPRESS
        )
        # findNetworkByRecordID_parser.add_argument("record_list")
        findNetworkByRecordID_parser.add_argument("record_list", type=list_of_tuples)
        findNetworkByRecordID_parser.add_argument("max_degrees", type=int)
        findNetworkByRecordID_parser.add_argument("build_out_degree", type=int)
        findNetworkByRecordID_parser.add_argument("max_entities", type=int)
        findNetworkByRecordID_parser.add_argument(
            "-f", "--flags", nargs="+", required=False
        )

        findPathByEntityID_parser = self.subparsers.add_parser(
            "findPathByEntityID", usage=argparse.SUPPRESS
        )
        findPathByEntityID_parser.add_argument("start_entity_id", type=int)
        findPathByEntityID_parser.add_argument("end_entity_id", type=int)
        findPathByEntityID_parser.add_argument("max_degrees", type=int)
        # TODO nargs needs to change if accepting lists instead of json
        findPathByEntityID_parser.add_argument(
            "-e", "--exclusions", default="", nargs="?", required=False
        )
        findPathByEntityID_parser.add_argument(
            "-r", "--required_data_sources", default="", nargs="?", required=False
        )
        findPathByEntityID_parser.add_argument(
            "-f", "--flags", nargs="+", required=False
        )

        findPathByRecordID_parser = self.subparsers.add_parser(
            "findPathByRecordID", usage=argparse.SUPPRESS
        )
        findPathByRecordID_parser.add_argument("start_data_source_code")
        findPathByRecordID_parser.add_argument("start_record_id")
        findPathByRecordID_parser.add_argument("end_data_source_code")
        findPathByRecordID_parser.add_argument("end_record_id")
        findPathByRecordID_parser.add_argument("max_degrees", type=int)
        # TODO nargs needs to change if accepting lists instead of json
        findPathByRecordID_parser.add_argument(
            "-e", "--exclusions", default="", nargs="?", required=False
        )
        findPathByRecordID_parser.add_argument(
            "-r", "--required_data_sources", default="", nargs="?", required=False
        )
        findPathByRecordID_parser.add_argument(
            "-f", "--flags", nargs="+", required=False
        )

        getEntityByEntityID_parser = self.subparsers.add_parser(
            "getEntityByEntityID", usage=argparse.SUPPRESS
        )
        getEntityByEntityID_parser.add_argument("entity_id", type=int)
        getEntityByEntityID_parser.add_argument(
            "-f", "--flags", nargs="+", required=False
        )

        getEntityByRecordID_parser = self.subparsers.add_parser(
            "getEntityByRecordID", usage=argparse.SUPPRESS
        )
        getEntityByRecordID_parser.add_argument("data_source_code")
        getEntityByRecordID_parser.add_argument("record_id")
        getEntityByRecordID_parser.add_argument(
            "-f", "--flags", nargs="+", required=False
        )

        getRecord_parser = self.subparsers.add_parser(
            "getRecord", usage=argparse.SUPPRESS
        )
        getRecord_parser.add_argument("data_source_code")
        getRecord_parser.add_argument("record_id")
        getRecord_parser.add_argument("-f", "--flags", nargs="+", required=False)

        getVirtualEntityByRecordID_parser = self.subparsers.add_parser(
            "getVirtualEntityByRecordID", usage=argparse.SUPPRESS
        )
        getVirtualEntityByRecordID_parser.add_argument("record_list")
        getVirtualEntityByRecordID_parser.add_argument(
            "-f", "--flags", nargs="+", required=False
        )

        howEntityByEntityID_parser = self.subparsers.add_parser(
            "howEntityByEntityID", usage=argparse.SUPPRESS
        )
        howEntityByEntityID_parser.add_argument("entity_id", type=int)
        howEntityByEntityID_parser.add_argument(
            "-f", "--flags", nargs="+", required=False
        )

        processRedoRecord_parser = self.subparsers.add_parser(
            "processRedoRecord", usage=argparse.SUPPRESS
        )
        processRedoRecord_parser.add_argument("redo_record")
        processRedoRecord_parser.add_argument(
            "-f", "--flags", nargs="+", required=False
        )

        reevaluateEntity_parser = self.subparsers.add_parser(
            "reevaluateEntity", usage=argparse.SUPPRESS
        )
        reevaluateEntity_parser.add_argument("entity_id", type=int)
        reevaluateEntity_parser.add_argument("-f", "--flags", required=False, type=int)

        reevaluateRecord_parser = self.subparsers.add_parser(
            "reevaluateRecord", usage=argparse.SUPPRESS
        )
        reevaluateRecord_parser.add_argument("data_source_code")
        reevaluateRecord_parser.add_argument("record_id")
        reevaluateRecord_parser.add_argument("-f", "--flags", required=False, type=int)

        # replaceRecord_parser = self.subparsers.add_parser(
        #     "replaceRecord", usage=argparse.SUPPRESS
        # )
        # replaceRecord_parser.add_argument("data_source_code")
        # replaceRecord_parser.add_argument("record_id")
        # replaceRecord_parser.add_argument("record_definition")
        # replaceRecord_parser.add_argument("-f", "--flags", nargs="+", required=False)

        searchByAttributes_parser = self.subparsers.add_parser(
            "searchByAttributes", usage=argparse.SUPPRESS
        )
        searchByAttributes_parser.add_argument("attributes")
        # TODO Remove default
        searchByAttributes_parser.add_argument(
            "search_profile", default="SEARCH", nargs="?"
        )
        searchByAttributes_parser.add_argument(
            "-f", "--flags", nargs="+", required=False
        )

        whyEntities_parser = self.subparsers.add_parser(
            "whyEntities", usage=argparse.SUPPRESS
        )
        whyEntities_parser.add_argument("entity_id1", type=int)
        whyEntities_parser.add_argument("entity_id2", type=int)
        whyEntities_parser.add_argument("-f", "--flags", nargs="+", required=False)

        whyRecordInEntity_parser = self.subparsers.add_parser(
            "whyRecordInEntity", usage=argparse.SUPPRESS
        )
        whyRecordInEntity_parser.add_argument("data_source_code")
        whyRecordInEntity_parser.add_argument("record_id")
        whyRecordInEntity_parser.add_argument(
            "-f", "--flags", nargs="+", required=False
        )

        whyRecords_parser = self.subparsers.add_parser(
            "whyRecords", usage=argparse.SUPPRESS
        )
        whyRecords_parser.add_argument("data_source_code1")
        whyRecords_parser.add_argument("record_id1")
        whyRecords_parser.add_argument("data_source_code2")
        whyRecords_parser.add_argument("record_id2")
        whyRecords_parser.add_argument("-f", "--flags", nargs="+", required=False)

        # Utility parsers

        addConfigFile_parser = self.subparsers.add_parser(
            "addConfigFile", usage=argparse.SUPPRESS
        )
        addConfigFile_parser.add_argument("config_json_file")
        addConfigFile_parser.add_argument("config_comments")

        processFile_parser = self.subparsers.add_parser(
            "processFile", usage=argparse.SUPPRESS
        )
        processFile_parser.add_argument("input_file")

        responseToFile_parser = self.subparsers.add_parser(
            "responseToFile", usage=argparse.SUPPRESS
        )
        responseToFile_parser.add_argument("file_path")

        setOutputColor_parser = self.subparsers.add_parser(
            "setOutputColor", usage=argparse.SUPPRESS
        )
        setOutputColor_parser.add_argument("output_color", nargs="?")

        setOutputFormat_parser = self.subparsers.add_parser(
            "setOutputFormat", usage=argparse.SUPPRESS
        )
        setOutputFormat_parser.add_argument("output_format", nargs="?")

        setTheme_parser = self.subparsers.add_parser(
            "setTheme", usage=argparse.SUPPRESS
        )
        setTheme_parser.add_argument("theme", choices=["light", "default"], nargs=1)

    # Override function from cmd module to make command completion case-insensitive
    def completenames(self, text, *ignored):
        do_text = "do_" + text
        return [
            a[3:] for a in self.get_names() if a.lower().startswith(do_text.lower())
        ]

    # Override base method in cmd module to return methods for autocomplete and help
    def get_names(self, include_hidden=False):
        if not include_hidden:
            return [n for n in dir(self.__class__) if n not in self.__hidden_methods]

        return list(dir(self.__class__))

    def preloop(self):
        if self.initialized:
            return
        self.print_response(
            colorize_msg("Welcome to szcommand. Type help or ? for help", "highlight2")
        )

    def postloop(self):
        self.initialized = False

    def precmd(self, line):
        return cmd.Cmd.precmd(self, line)

    def postcmd(self, stop, line):
        # If restart has been requested, set stop value to True to restart engines in main loop
        if self.restart:
            return cmd.Cmd.postcmd(self, True, line)

        return cmd.Cmd.postcmd(self, stop, line)

    @staticmethod
    def do_quit(_):
        return True

    def do_exit(self, _):
        self.do_quit(self)
        return True

    def ret_quit(self):
        return self.quit

    @staticmethod
    def do_EOF(_):
        return True

    def emptyline(self):
        return

    def default(self, line):
        self.print_error("Unknown command, type help or ?")
        return

    def cmdloop(self, intro=None):
        while True:
            try:
                super(SzCmdShell, self).cmdloop(intro=self.intro)
                break
            except KeyboardInterrupt:
                if input(
                    colorize_msg("\n\nAre you sure you want to exit? (y/n) ", "caution")
                ) in ["y", "Y", "yes", "YES"]:
                    break
                else:
                    print()
            except TypeError as ex:
                self.print_error(ex)

    def fileloop(self, file_name):
        self.preloop()

        with open(file_name) as data_in:
            for line in data_in:
                line = line.strip()
                # Ignore comments and blank lines
                if len(line) > 0 and line[0:1] not in ("#", "-", "/"):
                    # *args allows for empty list if there are no args
                    (read_cmd, *args) = line.split()
                    process_cmd = f"do_{read_cmd}"
                    self.print_with_new_lines(f"----- {read_cmd} -----", "S")
                    self.print_with_new_lines(f"{line}", "S")

                    if process_cmd not in dir(self):
                        self.print_error(f"Command {read_cmd} not found")
                    else:
                        # Join the args into a printable string, format into the command + args to call
                        try:
                            exec_cmd = f'self.{process_cmd}({repr(" ".join(args))})'
                            exec(exec_cmd)
                        except (ValueError, TypeError) as ex:
                            self.print_error("Command could not be run!")
                            self.print_error(ex)

    def do_hidden(self, _):
        self.print_response(self.__hidden_methods)

    # ----- Help -----
    # ===== custom help section =====
    def do_help(self, help_topic):
        if not help_topic:
            self.help_overview()
            return

        if help_topic not in self.get_names(include_hidden=True):
            help_topic = "do_" + help_topic
            if help_topic not in self.get_names(include_hidden=True):
                cmd.Cmd.do_help(self, help_topic[3:])
                return

        topic_docstring = getattr(self, help_topic).__doc__
        if not topic_docstring:
            self.print_response(
                colorize_msg(f"No help found for {help_topic[3:]}", "warning")
            )
            return

        help_text = current_section = ""
        headers = [
            "Syntax:",
            "Examples:",
            "Example:",
            "Notes:",
            "Caution:",
            "Arguments:",
        ]

        if cli_args.colorDisable:
            print(textwrap.dedent(topic_docstring))
            return

        help_lines = textwrap.dedent(topic_docstring).split("\n")

        for line in help_lines:
            line_color = ""
            if line:
                if line in headers:
                    line_color = "highlight2"
                    current_section = line

                if current_section == "Caution:":
                    line_color = "caution, italics"
                elif current_section not in (
                    "Syntax:",
                    "Examples:",
                    "Example:",
                    "Notes:",
                    "Arguments:",
                ):
                    line_color = ""

            if re.match(rf"^\s*{help_topic[3:]}", line) and not line_color:
                sep_column = line.find(help_topic[3:]) + len(help_topic[3:])
                help_text += (
                    line[0:sep_column] + colorize(line[sep_column:], "dim") + "\n"
                )
            else:
                help_text += colorize(line, line_color) + "\n"

        print(help_text)

    def help_all(self):
        cmd.Cmd.do_help(self, "")

    @staticmethod
    def help_overview():
        print(
            textwrap.dedent(
                f"""
        {colorize('This utility allows you to interact with the Senzing APIs.', 'dim')}

        {colorize('Help', 'highlight2')}
            {colorize('- View help for a command:', 'dim')} help COMMAND
            {colorize('- View all commands:', 'dim')} help all

        {colorize('Tab Completion', 'highlight2')}
            {colorize('- Tab completion is available for commands, files and engine flags', 'dim')}
            {colorize('- Hit tab on a blank line to see all commands', 'dim')}

        {colorize('JSON Formatting', 'highlight2')}
            {colorize('- Change JSON formatting by adding "json" or "jsonl" to the end of a command', 'dim')}
                - getEntityByEntityID 1001 jsonl
                
            {colorize('- Can be combined with color formatting options', 'dim')}
                - getEntityByEntityID 1001 jsonl nocolor
                
            {colorize('- Set the JSON format for the session, saves the preference to a configuration file for use across sessions', 'dim')}
            {colorize('- Specifying the JSON and color formatting options at the end of a command override this setting for that command', 'dim')}
                - setOutputFormat json|jsonl
                
            {colorize('- Convert last response output between json and jsonl', 'dim')}
                - responseReformatJson
                
        {colorize('Color Formatting', 'highlight2')}
            {colorize('- Add or remove colors from JSON formatting by adding "color", "colour", "nocolor" or "nocolour" to the end of a command', 'dim')}
                - getEntityByEntityID 1001 color
                
            {colorize('- Can be combined with JSON formatting options', 'dim')}
                - getEntityByEntityID 1001 color jsonl
                
            {colorize('- Set the color formatting for the session, saves the preference to a configuration file for use across sessions', 'dim')}
            {colorize('- Specifying the JSON and color formatting options at the end of a command override this setting for that command', 'dim')}
                - setOutputColor color|colour|nocolor|nocolour
                                
        {colorize('Capturing Output', 'highlight2')}
            {colorize('- Capture the last response output to a file or the clipboard', 'dim')}
                - responseToClipboard
                - responseToFile /tmp/myoutput.json
            {colorize('- responseToClipboard does not work in containers or SSH sessions', 'dim')}

        {colorize('History', 'highlight2')}
            {colorize('- Arrow keys to cycle through history of commands', 'dim')}
            {colorize('- Ctrl-r can be used to search history', 'dim')}
            {colorize('- Display history:', 'dim')} history

        {colorize('Timer', 'highlight2')}
            {colorize('- Toggle on/off approximate time a command takes to complete', 'dim')}
            {colorize('- Turn off JSON formatting and color output for higher accuracy', 'dim')}
                - timer
                
        {colorize('Shell', 'highlight2')}
            {colorize('- Run basic OS shell commands', 'dim')}
                - ! ls
                
        {colorize('Support', 'highlight2')}
            {colorize('- Senzing Support:', 'dim')} {colorize('https://senzing.zendesk.com/hc/en-us/requests/new', 'highlight1,underline')}
            {colorize('- Senzing Knowledge Center:', 'dim')} {colorize('https://senzing.zendesk.com/hc/en-us', 'highlight1,underline')}
            {colorize('- API Docs:', 'dim')} {colorize('https://docs.senzing.com', 'highlight1,underline')}

        """
            )
        )

    def do_shell(self, line):
        print(os.popen(line).read())

    def hist_check(self):
        """Attempt to set up history"""

        if not self.hist_disable:
            if readline_avail:
                tmpHist = "." + os.path.basename(
                    sys.argv[0].lower().replace(".py", "_history")
                )
                self.hist_file_name = os.path.join(os.path.expanduser("~"), tmpHist)

                # Try and open history in users home first for longevity
                try:
                    open(self.hist_file_name, "a").close()
                except IOError as err:
                    self.histFileError = f"{err} - Couldn't use home, trying /tmp/..."
                    # Can't use users home, try using /tmp/ for history useful at least in the session
                    self.hist_file_name = f"/tmp/{tmpHist}"
                    try:
                        open(self.hist_file_name, "a").close()
                    except IOError as err:
                        self.histFileError = f"{err} - User home dir and /tmp/ failed!"
                        return

                hist_size = 2000
                readline.read_history_file(self.hist_file_name)
                readline.set_history_length(hist_size)
                atexit.register(readline.set_history_length, hist_size)
                atexit.register(readline.write_history_file, self.hist_file_name)

                self.histFileError = None
                self.hist_avail = True

    # ----- Senzing Commands -----

    # szconfig commands

    # TODO Add a note this isn't an API?
    # TODO Reorder
    @cmd_decorator()
    def do_getConfig(self, **kwargs):
        """
        Get a configuration

        Syntax:
            getConfig CONFIG_ID

        Example:
            getConfig 4180061352

        Arguments:
            CONFIG_ID = Configuration identifier

        Notes:
            - Retrieve the active configuration identifier with getActiveConfigID

            - Retrieve a list of configurations and identifiers with getConfigList"""

        response = self.sz_configmgr.get_config(kwargs["parsed_args"].config_id)
        self.print_response(response)

    @cmd_decorator(cmd_has_args=False)
    def do_getTemplateConfig(self, **kwargs):
        """
        Get a template configuration

        Syntax:
            getTemplateConfig"""

        configHandle = self.sz_config.create_config()
        response = self.sz_config.export_config(configHandle)
        self.sz_config.close_config(configHandle)
        self.print_response(response)

    # szconfigmgr commands

    @cmd_decorator(cmd_has_args=False)
    def do_getConfigs(self, **kwargs):
        """
        Get a list of current configurations

        Syntax:
            getConfigList"""

        response = self.sz_configmgr.get_configs()
        self.print_response(response)

    @cmd_decorator(cmd_has_args=False)
    def do_getDefaultConfigID(self, **kwargs):
        """
        Get the default configuration ID

        Syntax:
            getDefaultConfigID"""

        response = self.sz_configmgr.get_default_config_id()
        self.print_response(response, "success")

    @cmd_decorator()
    def do_replaceDefaultConfigID(self, **kwargs):
        """
        Replace the default configuration ID

        Syntax:
            replaceDefaultConfigID CURRENT_DEFAULT_CONFIG_ID NEW_DEFAULT_CONFIG_ID

        Example:
            replaceDefaultConfigID 4180061352 2787925967

        Arguments:
            CURRENT_DEFAULT_CONFIG_ID = Configuration identifier
            NEW_DEFAULT_CONFIG_ID = Configuration identifier

        Notes:
            - Retrieve a list of configurations and identifiers with getConfigList"""

        self.sz_configmgr.replace_default_config_id(
            kwargs["parsed_args"].current_default_config_id,
            kwargs["parsed_args"].new_default_config_id,
        )
        self.print_response("New default config set, restarting engines...", "success")
        self.do_restart(None) if not self.debug_trace else self.do_restartDebug(None)

    @cmd_decorator()
    def do_setDefaultConfigID(self, **kwargs):
        """
        Set the default configuration ID

        Syntax:
            setDefaultConfigID CONFIG_ID

        Example:
            setDefaultConfigID 4180061352

        Arguments:
            CONFIG_ID = Configuration identifier

        Notes:
            - Retrieve a list of configurations and identifiers with getConfigList"""

        self.sz_configmgr.set_default_config_id(kwargs["parsed_args"].config_id)
        self.print_response("Default config set, restarting engines...", "success")
        self.do_restart(None) if not self.debug_trace else self.do_restartDebug(None)

    # szdiagnostic commands

    @cmd_decorator()
    def do_checkDatastorePerformance(self, **kwargs):
        """
        Run a performance check on the database

        Syntax:
            checkDatastorePerformance [SECONDS]
            checkDatastorePerformance

        Arguments:
            SECONDS = Time in seconds to run check, default is 3"""

        response = self.sz_diagnostic.check_datastore_performance(
            kwargs["parsed_args"].secondsToRun
        )
        self.print_response(response)

    @cmd_decorator(cmd_has_args=False)
    def do_getDatastoreInfo(self, **kwargs):
        """
        Get data store information

        Syntax:
            getDatastoreInfo"""

        response = self.sz_diagnostic.get_datastore_info()
        self.print_response(response)

    @cmd_decorator()
    def do_getFeature(self, **kwargs):
        """
        Get feature information

        Syntax:
            getFeature FEATURE_ID

        Examples:
            getFeature 1

        Arguments:
            FEATURE_ID = Identifier of feature"""

        response = self.sz_diagnostic.get_feature(kwargs["parsed_args"].featureID)
        self.print_response(response)

    @cmd_decorator()
    def do_purgeRepository(self, **kwargs):
        """
        Purge Senzing database of all data

        Syntax:
            purgeRepository [--FORCEPURGE]

        Example:
            purgeRepository

        Arguments:
            --FORCEPURGE = Don't prompt before purging. USE WITH CAUTION!

        Caution:
            - This deletes all data in the Senzing database!"""

        purge_msg = colorize_msg(
            textwrap.dedent(
                """
            
                ********** WARNING **********
                
                This will purge all currently loaded data from the senzing database!
                Before proceeding, all instances of senzing (custom code, rest api, redoer, etc.) must be shut down.
                
                ********** WARNING **********
                
                Are you sure you want to purge the senzing database? (y/n) """
            ),
            "warning",
        )

        if not kwargs["parsed_args"].force_purge:
            if input(purge_msg) not in ["y", "Y", "yes", "YES"]:
                print()
                return

        # if kwargs["parsed_args"].noReset:
        #     reset_resolver = False
        #     resolver_txt = "(without resetting resolver)"
        # else:
        #     reset_resolver = True
        #     resolver_txt = "(and resetting resolver)"

        # self.printResponse(f"Purging the Senzing database {resolver_txt}...", "info")
        # self.sz_engine.purgeRepository(reset_resolver)
        self.sz_diagnostic.purge_repository()

    # szengine commands

    @cmd_decorator()
    def do_addRecord(self, **kwargs):
        """
        Add a record and optionally return information

        Syntax:
            addRecord DSRC_CODE RECORD_ID RECORD_DEFINITION [-f FLAG ...]

        Examples:
            addRecord test 1 '{"NAME_FULL":"Robert Smith", "DATE_OF_BIRTH":"7/4/1976", "PHONE_NUMBER":"787-767-2088"}'
            addRecord test 1 '{"NAME_FULL":"Robert Smith", "DATE_OF_BIRTH":"7/4/1976", "PHONE_NUMBER":"787-767-2088"}' -f SZ_WITH_INFO

        Arguments:
            DSRC_CODE = Data source code
            RECORD_ID = Record identifier
            RECORD_DEFINITION = Senzing mapped JSON representation of a record
            FLAG = Optional space separated list of engine flag(s) to determine output (don't specify for defaults)
        """
        response = self.sz_engine.add_record(
            kwargs["parsed_args"].data_source_code,
            kwargs["parsed_args"].record_id,
            kwargs["parsed_args"].record_definition,
            **kwargs["flags_dict"],
        )

        if response == "{}":
            self.print_response("Record added.", "success")
        else:
            self.print_response(response)

    @cmd_decorator(cmd_has_args=False)
    def do_countRedoRecords(self, **kwargs):
        """
        Counts the number of records in the redo queue

        Syntax:
            countRedoRecords"""

        response = self.sz_engine.count_redo_records()
        if not response:
            self.print_response("No redo records.", "info")
        else:
            self.print_response(response, "success")

    @cmd_decorator()
    def do_deleteRecord(self, **kwargs):
        """
        Delete a record and optionally return information

        Syntax:
            deleteRecord DSRC_CODE RECORD_ID [-f FLAG ...]

        Examples:
            deleteRecord test 1
            deleteRecord test 1 -f SZ_WITH_INFO

        Arguments:
            DSRC_CODE = Data source code
            RECORD_ID = Record identifier
            FLAG = Optional space separated list of engine flag(s) to determine output (don't specify for defaults)
        """

        response = self.sz_engine.delete_record(
            kwargs["parsed_args"].data_source_code,
            kwargs["parsed_args"].record_id,
            **kwargs["flags_dict"],
        )

        if response == "{}":
            self.print_response("Record deleted.", "success")
        else:
            self.print_response(response)

    # TODO Fix flag names and check all still valid
    # TODO Check available columns for V4
    @cmd_decorator()
    def do_exportCSVEntityReport(self, **kwargs):
        """
        Export repository contents as CSV

        Syntax:
            exportCSVEntityReport OUTPUT_FILE [-t CSV_COLUMN_LIST,...] [-f FLAG ...]

        Examples:
            exportCSVEntityReport export.csv
            exportCSVEntityReport export.csv -t RESOLVED_ENTITY_ID,RELATED_ENTITY_ID,MATCH_LEVEL,MATCH_KEY,DATA_SOURCE,RECORD_ID
            exportCSVEntityReport export.csv -f SZ_EXPORT_INCLUDE_RESOLVED SZ_EXPORT_INCLUDE_POSSIBLY_SAME

        Arguments:
            OUTPUT_FILE = File to save export to
            CSV_COLUMN_LIST = Comma separated list of output columns (don't specify for defaults)
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Available CSV_COLUMNs
                - RESOLVED_ENTITY_ID,RELATED_ENTITY_ID,MATCH_LEVEL,MATCH_KEY,DATA_SOURCE,RECORD_ID,RESOLVED_ENTITY_NAME,RECORD_DEFINITION,ERRULE_CODE

            - Engine flag details https://docs.senzing.com/flags/index.html

        Caution:
            - Export isn't intended for exporting large numbers of entities and associated data source record information.
              Beyond 100M+ data source records isn't suggested. For exporting overview entity and relationship data for
              analytical purposes outside of Senzing please review the following article.

              https://senzing.zendesk.com/hc/en-us/articles/360010716274--Advanced-Replicating-the-Senzing-results-to-a-Data-Warehouse
        """

        rec_cnt = 0

        try:
            with open(kwargs["parsed_args"].output_file, "w") as data_out:
                export_handle = self.sz_engine.export_csv_entity_report(
                    kwargs["parsed_args"].csv_column_list, **kwargs["flags_dict"]
                )

                while True:
                    export_record = self.sz_engine.fetch_next(export_handle)
                    if not export_record:
                        break
                    data_out.write(export_record)
                    rec_cnt += 1
                    if rec_cnt % 1000 == 0:
                        print(f"Exported {rec_cnt} records...", flush=True)

                self.sz_engine.close_export(export_handle)
        except (SzError, IOError) as err:
            self.print_error(err)
        else:
            self.print_response(f"Total exported records: {rec_cnt}", "success")

    @cmd_decorator()
    def do_exportJSONEntityReport(self, **kwargs):
        """
        Export repository contents as JSON

        Syntax:
            exportJSONEntityReport OUTPUT_FILE [-f FLAG ...]

        Examples:
            exportJSONEntityReport export.json
            exportJSONEntityReport export.json -f SZ_EXPORT_INCLUDE_RESOLVED SZ_EXPORT_INCLUDE_POSSIBLY_SAME

        Arguments:
            OUTPUT_FILE = File to save export to
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html

        Caution:
            - Export isn't intended for exporting large numbers of entities and associated data source record information.
              Beyond 100M+ data source records isn't suggested. For exporting overview entity and relationship data for
              analytical purposes outside of Senzing please review the following article.

              https://senzing.zendesk.com/hc/en-us/articles/360010716274--Advanced-Replicating-the-Senzing-results-to-a-Data-Warehouse
        """

        rec_cnt = 0

        try:
            with open(kwargs["parsed_args"].output_file, "w") as data_out:
                export_handle = self.sz_engine.export_json_entity_report(
                    **kwargs["flags_dict"]
                )
                while True:
                    export_record = self.sz_engine.fetch_next(export_handle)
                    if not export_record:
                        break
                    data_out.write(export_record)
                    rec_cnt += 1
                    if rec_cnt % 1000 == 0:
                        print(f"Exported {rec_cnt} records...", flush=True)

                self.sz_engine.close_export(export_handle)
        except (SzError, IOError) as err:
            self.print_error(err)
        else:
            self.print_response(f"Total exported records: {rec_cnt}", "success")

    @cmd_decorator()
    def do_findInterestingEntitiesByEntityID(self, **kwargs):
        """
        Find interesting entities close to an entity by resolved entity identifier

        Syntax:
            findInterestingEntitiesByEntityID ENTITY_ID [-f FLAG ...]

        Example:
            findInterestingEntitiesByEntityID 1

        Arguments:
            ENTITY_ID = Identifier for an entity
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html

            - Experimental feature requires additional configuration, contact support@senzing.com
        """

        response = self.sz_engine.find_interesting_entities_by_entity_id(
            kwargs["parsed_args"].entity_id, **kwargs["flags_dict"]
        )
        self.print_response(response)

    @cmd_decorator()
    def do_findInterestingEntitiesByRecordID(self, **kwargs):
        """
        Find interesting entities close to an entity by record identifier

        Syntax:
            findInterestingEntitiesByRecordID DSRC_CODE RECORD_ID [-f FLAG ...]

        Example:
            findInterestingEntitiesByRecordID customers 1001

        Arguments:
            DSRC_CODE = Data source code
            RECORD_ID = Record identifier
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html

            - Experimental feature requires additional configuration, contact support@senzing.com
        """

        response = self.sz_engine.find_interesting_entities_by_record_id(
            kwargs["parsed_args"].data_source_code,
            kwargs["parsed_args"].record_id,
            **kwargs["flags_dict"],
        )
        self.print_response(response)

    @cmd_decorator()
    def do_findNetworkByEntityID(self, **kwargs):
        """
        Find network between entities

        Syntax:
            findNetworkByEntityID ENTITY_LIST MAX_DEGREES BUILD_OUT_DEGREE MAX_ENTITIES [-f FLAG ...]

        Example:
            findNetworkByEntityID '{"ENTITIES":[{"ENTITY_ID":"6"},{"ENTITY_ID":"11"},{"ENTITY_ID":"9"}]}' 4 3 20

        Arguments:
            ENTITY_LIST = JSON document listing entities to find paths between and networks around
            MAX_DEGREES = Maximum number of relationships to search for a path
            BUILD_OUT_DEGREE = Maximum degree of relationships to include around each entity
            MAX_ENTITIES = Maximum number of entities to return
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        response = self.sz_engine.find_network_by_entity_id(
            kwargs["parsed_args"].entity_list,
            kwargs["parsed_args"].max_degrees,
            kwargs["parsed_args"].build_out_degree,
            kwargs["parsed_args"].max_entities,
            **kwargs["flags_dict"],
        )
        self.print_response(response)

    @cmd_decorator()
    def do_findNetworkByRecordID(self, **kwargs):
        """
        Find network between records

        Syntax:
            findNetworkByRecordID RECORD_LIST MAX_DEGREES BUILD_OUT_DEGREE MAX_ENTITIES [-f FLAG ...]

        Example:
            findNetworkByRecordID '{"RECORDS":[{"DATA_SOURCE":"REFERENCE","RECORD_ID":"2071"},{"DATA_SOURCE":"CUSTOMERS","RECORD_ID":"1069"}]}' 6 4 15

        Arguments:
            RECORD_LIST = JSON document listing records to find paths between and networks around
            MAX_DEGREES = Maximum number of relationships to search for a path
            BUILD_OUT_DEGREE = Maximum degree of relationships to include around each entity
            MAX_ENTITIES = Maximum number of entities to return
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        response = self.sz_engine.find_network_by_record_id(
            kwargs["parsed_args"].record_list,
            kwargs["parsed_args"].max_degrees,
            kwargs["parsed_args"].build_out_degree,
            kwargs["parsed_args"].max_entities,
            **kwargs["flags_dict"],
        )
        self.print_response(response)

    @cmd_decorator()
    def do_findPathByEntityID(self, **kwargs):
        """
        Find a path between two entities

        Syntax:
            findPathByEntityID START_ENTITY_ID END_ENTITY_ID MAX_DEGREES [-e EXCLUSIONS] [-r REQUIRED_DATA_SOURCES] [-f FLAG ...]

        Example:
            findPathByEntityID 100002 5 3

        Arguments:
            START_ENTITY_ID = Identifier for an entity
            END_ENTITY_ID = Identifier for an entity
            MAX_DEGREES = Maximum number of relationships to search for a path
            EXCLUSIONS = Exclude specified entity IDs or record IDs from the path, default is no exclusions
            REQUIRED_DATA_SOURCES = An entity on the path has specified data source(s), default is no required data sources
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        response = self.sz_engine.find_path_by_entity_id(
            kwargs["parsed_args"].start_entity_id,
            kwargs["parsed_args"].end_entity_id,
            kwargs["parsed_args"].max_degrees,
            kwargs["parsed_args"].exclusions,
            kwargs["parsed_args"].required_data_sources,
            **kwargs["flags_dict"],
        )
        self.print_response(response)

    # TODO Wording on exclusions
    # TODO Examples with list of entity ids when szengine supports it
    # TODO EXCLUSIONS ... ?
    # TODO Autocomplete data sources? And on other methods?
    @cmd_decorator()
    def do_findPathByRecordID(self, **kwargs):
        """
        Find a path between two records

        Syntax:
            findPathByRecordID START_DSRC_CODE START_RECORD_ID END_DSRC_CODE END_RECORD_ID MAX_DEGREES [-e EXCLUSIONS] [-r REQUIRED_DATA_SOURCES] [-f FLAG ...]

        Example:
            findPathByRecordID reference 2141 reference 2121 6

        Arguments:
            START_DSRC_CODE = Data source code
            START_RECORD_ID = Record identifier
            END_DSRC_CODE = Data source code
            END_RECORD_ID = Record identifier
            MAX_DEGREES = Maximum number of relationships to search for a path
            EXCLUSIONS = Exclude specified entity IDs or record IDs from the path, default is no exclusions
            REQUIRED_DATA_SOURCES = An entity on the path has specified data source(s), default is no required data sources
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        response = self.sz_engine.find_path_by_record_id(
            kwargs["parsed_args"].start_data_source_code,
            kwargs["parsed_args"].start_record_id,
            kwargs["parsed_args"].end_data_source_code,
            kwargs["parsed_args"].end_record_id,
            kwargs["parsed_args"].max_degrees,
            kwargs["parsed_args"].exclusions,
            kwargs["parsed_args"].required_data_sources,
            **kwargs["flags_dict"],
        )
        self.print_response(response)

    # TODO Wording on exclusions
    # TODO Examples with list of entity ids when szengine supports it
    # TODO EXCLUSIONS ... ?
    # TODO Autocomplete data sources? And on other methods?
    @cmd_decorator()
    def do_findPathByRecordID(self, **kwargs):
        """
        Find a path between two records

        Syntax:
            findPathByRecordID START_DSRC_CODE START_RECORD_ID END_DSRC_CODE END_RECORD_ID MAX_DEGREES [-e EXCLUSIONS] [-r REQUIRED_DATA_SOURCES] [-f FLAG ...]

        Example:
            findPathByRecordID reference 2141 reference 2121 6

        Arguments:
            START_DSRC_CODE = Data source code
            START_RECORD_ID = Record identifier
            END_DSRC_CODE = Data source code
            END_RECORD_ID = Record identifier
            MAX_DEGREES = Maximum number of relationships to search for a path
            EXCLUSIONS = Exclude specified entity IDs or record IDs from the path, default is no exclusions
            REQUIRED_DATA_SOURCES = An entity on the path has specified data source(s), default is no required data sources
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        response = self.sz_engine.find_path_by_record_id(
            kwargs["parsed_args"].start_data_source_code,
            kwargs["parsed_args"].start_record_id,
            kwargs["parsed_args"].end_data_source_code,
            kwargs["parsed_args"].end_record_id,
            kwargs["parsed_args"].max_degrees,
            kwargs["parsed_args"].exclusions,
            kwargs["parsed_args"].required_data_sources,
            **kwargs["flags_dict"],
        )
        self.print_response(response)

    @cmd_decorator(cmd_has_args=False)
    def do_getActiveConfigID(self, **kwargs):
        """
        Get the active configuration identifier

        Syntax:
            getActiveConfigID"""

        response = self.sz_engine.get_active_config_id()
        self.print_response(response, "success")

    @cmd_decorator()
    def do_getEntityByEntityID(self, **kwargs):
        """
        Get entity by resolved entity identifier

        Syntax:
            getEntityByEntityID ENTITY_ID [-f FLAG ...]

        Examples:
            getEntityByEntityID 1
            getEntityByEntityID 1 -f SZ_ENTITY_BRIEF_DEFAULT_FLAGS SZ_ENTITY_INCLUDE_RECORD_SUMMARY

        Arguments:
            ENTITY_ID = Identifier for an entity
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        response = self.sz_engine.get_entity_by_entity_id(
            kwargs["parsed_args"].entity_id, **kwargs["flags_dict"]
        )
        self.print_response(response)

    @cmd_decorator()
    def do_getEntityByRecordID(self, **kwargs):
        """
        Get entity by data source code and record identifier

        Syntax:
            getEntityByRecordID DSRC_CODE RECORD_ID [-f FLAG ...]

        Examples:
        getEntityByRecordID customers 1001
        getEntityByRecordID customers 1001 -f SZ_ENTITY_BRIEF_DEFAULT_FLAGS SZ_ENTITY_INCLUDE_RECORD_SUMMARY

        Arguments:
            DSRC_CODE = Data source code
            RECORD_ID = Record identifier
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        response = self.sz_engine.get_entity_by_record_id(
            kwargs["parsed_args"].data_source_code,
            kwargs["parsed_args"].record_id,
            **kwargs["flags_dict"],
        )
        self.print_response(response)

    @cmd_decorator()
    def do_getRecord(self, **kwargs):
        """
        Get a record

        Syntax:
            getRecord DSRC_CODE RECORD_ID [-f FLAG ...]

        Examples:
            getRecord watchlist 2092
            getRecord watchlist 2092 -f SZ_RECORD_DEFAULT_FLAGS SZ_ENTITY_INCLUDE_RECORD_FORMATTED_DATA

        Arguments:
            DSRC_CODE = Data source code
            RECORD_ID = Record identifier
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        response = self.sz_engine.get_record(
            kwargs["parsed_args"].data_source_code,
            kwargs["parsed_args"].record_id,
            **kwargs["flags_dict"],
        )
        self.print_response(response)

    @cmd_decorator(cmd_has_args=False)
    def do_getRedoRecord(self, **kwargs):
        """
        Get a redo record from the redo queue

        Syntax:
            getRedoRecord"""

        response = self.sz_engine.get_redo_record()
        if not response:
            self.print_response("No redo records.", "info")
        else:
            self.print_response(response)

    @cmd_decorator(cmd_has_args=False)
    def do_getStats(self, **kwargs):
        """
        Get engine workload statistics for last process

        Syntax:
            getStats"""

        response = self.sz_engine.get_stats()
        self.print_response(response)

    @cmd_decorator()
    def do_getVirtualEntityByRecordID(self, **kwargs):
        """
        Determine how an entity composed of a given set of records would look

        Syntax:
            getVirtualEntityByRecordID RECORD_LIST[-f FLAG ...]

        Example:
            getVirtualEntityByRecordID '{"RECORDS": [{"DATA_SOURCE": "REFERENCE","RECORD_ID": "2071"},{"DATA_SOURCE": "CUSTOMERS","RECORD_ID": "1069"}]}'

        Arguments:
            RECORD_LIST = JSON document listing data sources and records
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        response = self.sz_engine.get_virtual_entity_by_record_id(
            kwargs["parsed_args"].record_list, **kwargs["flags_dict"]
        )
        self.print_response(response)

    @cmd_decorator()
    def do_howEntityByEntityID(self, **kwargs):
        """
        Retrieve information on how entities are constructed from their records

        Syntax:
            howEntityByEntityID ENTITY_ID [-f FLAG ...]

        Example:
            howEntityByEntityID 96

        Arguments:
            ENTITY_ID = Identifier for an entity
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        response = self.sz_engine.how_entity_by_entity_id(
            kwargs["parsed_args"].entity_id, **kwargs["flags_dict"]
        )
        self.print_response(response)

    @cmd_decorator(cmd_has_args=False)
    def do_primeEngine(self, **kwargs):
        """
        Prime the Senzing engine

        Syntax:
            primeEngine"""

        self.sz_engine.prime_engine()
        self.print_response("Engine primed.", "success")

    @cmd_decorator(cmd_has_args=True)
    def do_processRedoRecord(self, **kwargs):
        """
        Process a redo record fetched from the redo queue

        Syntax:
            processRedoRecord REDO_RECORD [-f FLAG ...]

        Examples:
            processRedoRecord <redo_record>
            processRedoRecord <redo_record> -f SZ_WITH_INFO

        Arguments:
            REDO_RECORD = A redo record
            FLAG = Optional space separated list of engine flag(s) to determine output (don't specify for defaults)
        """

        response = self.sz_engine.process_redo_record(
            kwargs["parsed_args"].redo_record,
            **kwargs["flags_dict"],
        )
        self.print_response(response)

    @cmd_decorator()
    def do_reevaluateEntity(self, **kwargs):
        """
        Reevaluate an entity and optionally return information

        Syntax:
            reevaluateEntity ENTITY_ID [-f FLAG ...]

        Example:
            reevaluateEntity 1

            reevaluateEntity 1 -f SZ_WITH_INFO

        Arguments:
            ENTITY_ID = Entity identifier
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        response = self.sz_engine.reevaluate_entity(
            kwargs["parsed_args"].entity_id, **kwargs["flags_dict"]
        )
        if response == "{}":
            self.print_response("Entity reevaluated.", "success")
        else:
            self.print_response(response)

    @cmd_decorator()
    def do_reevaluateRecord(self, **kwargs):
        """
        Reevaluate a record and optionally return information

        Syntax:
            reevaluateRecord DSRC_CODE RECORD_ID [-f FLAG ...]

        Examples:
            reevaluateRecord customers 1001
            reevaluateRecord customers 1001 -f SZ_WITH_INFO

        Arguments:
            DSRC_CODE = Data source code
            RECORD_ID = Record identifier
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        response = self.sz_engine.reevaluate_record(
            kwargs["parsed_args"].data_source_code,
            kwargs["parsed_args"].record_id,
            **kwargs["flags_dict"],
        )
        if response == "{}":
            self.print_response("Record reevaluated.", "success")
        else:
            self.print_response(response)

    # @cmd_decorator()
    # def do_replaceRecord(self, **kwargs):
    #     """
    #     Replace a record and optionally return information

    #     Syntax:
    #         replaceRecord DSRC_CODE RECORD_ID RECORD_DEFINITION [-f FLAG ...]

    #     Examples:
    #         replaceRecord test 1 '{"NAME_FULL":"John Smith", "DATE_OF_BIRTH":"7/4/1976", "PHONE_NUMBER":"787-767-2088"}'
    #         replaceRecord test 1 '{"NAME_FULL":"John Smith", "DATE_OF_BIRTH":"7/4/1976", "PHONE_NUMBER":"787-767-2088"}' -f SZ_WITH_INFO

    #     Arguments:
    #         DSRC_CODE = Data source code
    #         RECORD_ID = Record identifier
    #         RECORD_DEFINITION = Senzing mapped JSON representation of a record
    #         FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

    #     Notes:
    #         - Engine flag details https://docs.senzing.com/flags/index.html"""

    #     response = self.sz_engine.replace_record(
    #         kwargs["parsed_args"].data_source_code,
    #         kwargs["parsed_args"].record_id,
    #         kwargs["parsed_args"].record_definition,
    #         **kwargs["flags_dict"],
    #     )
    #     if response == "{}":
    #         self.print_response("Record replaced.", "success")
    #     else:
    #         self.print_response(response)

    @cmd_decorator()
    def do_searchByAttributes(self, **kwargs):
        """
        Search for entities

        Syntax:
            searchByAttributes ATTRIBUTES [SEARCH_PROFILE] [-f FLAG ...]

        Examples:
            searchByAttributes '{"name_full":"Robert Smith", "date_of_birth":"11/12/1978"}'
            searchByAttributes '{"name_full":"Robert Smith", "date_of_birth":"11/12/1978"}' SEARCH -f SZ_SEARCH_BY_ATTRIBUTES_MINIMAL_ALL

        Arguments:
            ATTRIBUTES = Senzing mapped JSON containing the attributes to search on
            SEARCH_PROFILE = Search profile to use (defaults to SEARCH)
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        print(type(kwargs["flags_dict"]))
        print(kwargs["flags_dict"])
        print(kwargs["flags_dict"]["flags"].value)
        response = self.sz_engine.search_by_attributes(
            kwargs["parsed_args"].attributes,
            # TODO Using like this here due to order of args in szengine
            kwargs["flags_dict"]["flags"].value,
            kwargs["parsed_args"].search_profile,
            # **kwargs["flags_dict"],
        )
        self.print_response(response)

    @cmd_decorator()
    def do_whyEntities(self, **kwargs):
        """
        Determine how entities relate to each other

        Syntax:
            whyEntities ENTITY_ID1 ENTITY_ID2 [-f FLAG ...]

        Examples:
            whyEntities 96 200011
            whyEntities 96 200011 -f SZ_WHY_ENTITY_DEFAULT_FLAGS SZ_ENTITY_INCLUDE_RECORD_RECORD_DEFINITION

        Arguments:
            ENTITY_ID1 = Identifier for first entity
            ENTITY_ID2 = Identifier for second entity
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        response = self.sz_engine.why_entities(
            kwargs["parsed_args"].entity_id1,
            kwargs["parsed_args"].entity_id2,
            **kwargs["flags_dict"],
        )
        self.print_response(response)

    @cmd_decorator()
    def do_whyRecordInEntity(self, **kwargs):
        """
        Determine why a particular record resolved to an entity

        Syntax:
            whyRecordInEntity DSRC_CODE RECORD_ID [-f FLAG ...]

        Examples:
            whyRecordInEntity reference 2121
            whyRecordInEntity reference 2121 -f SZ_WHY_ENTITY_DEFAULT_FLAGS SZ_ENTITY_INCLUDE_RECORD_RECORD_DEFINITION

        Arguments:
            DSRC_CODE = Data source code
            RECORD_ID = Record identifier
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        response = self.sz_engine.why_record_in_entity(
            kwargs["parsed_args"].data_source_code,
            kwargs["parsed_args"].record_id,
            **kwargs["flags_dict"],
        )
        self.print_response(response)

    @cmd_decorator()
    def do_whyRecords(self, **kwargs):
        """
        Determine how two records relate to each other

        Syntax:
            whyRecords DSRC_CODE1 RECORD_ID1 DSRC_CODE2 RECORD_ID1 [-f FLAG ...]

        Examples:
            whyRecords reference 2121 watchlist 2092
            whyRecords reference 2121 watchlist 2092 -f SZ_WHY_ENTITY_DEFAULT_FLAGS SZ_ENTITY_INCLUDE_RECORD_RECORD_DEFINITION

        Arguments:
            DSRC_CODE1 = Data source code for first record
            DSRC_CODE2 = Data source code for second record
            RECORD_ID1 = Identifier for first record
            RECORD_ID2 = Identifier for second record
            FLAG = Space separated list of engine flag(s) to determine output (don't specify for defaults)

        Notes:
            - Engine flag details https://docs.senzing.com/flags/index.html"""

        response = self.sz_engine.why_records(
            kwargs["parsed_args"].data_source_code1,
            kwargs["parsed_args"].record_id1,
            kwargs["parsed_args"].data_source_code2,
            kwargs["parsed_args"].record_id2,
            **kwargs["flags_dict"],
        )
        self.print_response(response)

    # szproduct commands

    @cmd_decorator(cmd_has_args=False)
    def do_getLicense(self, **kwargs):
        """
        Get the license information

        Syntax:
            getLicense"""

        self.print_response(self.sz_product.get_license())

    @cmd_decorator(cmd_has_args=False)
    def do_getVersion(self, **kwargs):
        """
        Get the version information

        Syntax:
            getVersion"""

        # TODO other places using dumps/loads where doesn't need to?
        # self.printResponse(json.dumps(json.loads(self.sz_product.get_version())))
        self.print_response(self.sz_product.get_version())

    # Helper commands

    # NOTE This isn't an API call
    # TODO Test
    @cmd_decorator()
    def do_addConfigFile(self, **kwargs):
        """
        Add a configuration from a file

        Syntax:
            addConfigFile CONFIG_FILE 'COMMENTS'

        Example:
            addConfigFile config.json 'Added new features'

        Arguments:
            CONFIG_FILE = File containing configuration to add
            COMMENTS = Comments for the configuration"""

        config = pathlib.Path(kwargs["parsed_args"].config_json_file).read_text()
        config = config.replace("\n", "")
        response = self.sz_configmgr.add_config(
            config, kwargs["parsed_args"].config_comments
        )
        self.print_response(f"Configuration added, ID = {response}", "success")

    def do_history(self, arg):

        if self.hist_avail:
            print()
            for i in range(readline.get_current_history_length()):
                self.print_with_new_lines(readline.get_history_item(i + 1))
            print()
        else:
            self.print_response("History isn't available in this session.", "caution")

    # TODO Add a note this isn't an API
    # TODO Reorder
    # TODO process() is no longer available would need to pull out details and action
    @cmd_decorator()
    def do_processFile(self, **kwargs):
        """
        Process a file of Senzing mapped records

        Syntax:
            processFile FILE

        Example:
            processFile demo/truth/customers.json

        Arguments:
            FILE = Input file containing Senzing mapped data records"""

        input_file = file_name = kwargs["parsed_args"].input_file
        data_source_parm = None
        cnt = 0

        if "/?" in input_file:
            file_name, data_source_parm = input_file.split("/?")
            if data_source_parm.upper().startswith("DATA_SOURCE="):
                data_source_parm = data_source_parm[12:].upper()

        _, file_extension = os.path.splitext(file_name)
        file_extension = file_extension[1:].upper()

        with open(file_name) as data_in:
            if file_extension != "CSV":
                file_reader = data_in
            else:
                file_reader = csv.reader(data_in)
                csvHeaders = [x.upper() for x in next(file_reader)]

            for line in file_reader:
                if file_extension != "CSV":
                    json_str = line.strip()
                else:
                    json_obj = dict(list(zip(csvHeaders, line)))
                    if data_source_parm:
                        json_obj["DATA_SOURCE"] = data_source_parm
                    json_str = json.dumps(json_obj)

                try:
                    self.sz_engine.process(json_str)
                except SzError as err:
                    self.print_error(err, f"At record {cnt + 1}")
                cnt += 1
                if cnt % 1000 == 0:
                    self.print_response(f"{cnt} records processed")
            self.print_response(f"{cnt} records processed", "success")

    def do_responseToClipboard(self, arg):
        def pyperclip_clip_msg():
            self.print_with_new_lines(
                colorize_msg(
                    textwrap.dedent(
                        """\
                        - The clipboard module is installed but no clipboard command could be found
                        
                        - This usually means xclip is missing on Linux and needs to be installed:
                            - sudo apt install xclip OR sudo yum install xclip
                            
                        - If you are running in a container or SSH lastResponseToClipboard cannot be used"""
                    ),
                    "info",
                ),
                "B",
            )

        if not pyperclip_avail:
            self.print_with_new_lines(
                colorize_msg(
                    textwrap.dedent(
                        """\
                        - To send the last response to the clipboard the Python module pyperclip needs to be installed
                            - pip install pyperclip
                            
                        - If you are running in a container or SSH lastResponseToClipboard cannot be used"""
                    ),
                    "info",
                ),
                "B",
            )
            return

        try:
            clip = pyperclip.determine_clipboard()
        except ModuleNotFoundError:
            pyperclip_clip_msg()
            return

        try:
            # If __name__ doesn't exist no clipboard tool was available
            _ = clip[0].__name__
        except AttributeError:
            pyperclip_clip_msg()
            return

        # This clipboard gets detected on Linux when xclip isn't installed, but it doesn't work
        if clip[0].__name__ == "copy_gi":
            pyperclip_clip_msg()
            return

        try:
            pyperclip.copy(self.last_response)
        except pyperclip.PyperclipException as err:
            self.print_error(err)

    @cmd_decorator()
    def do_responseToFile(self, **kwargs):
        with open(kwargs["parsed_args"].file_path, "w") as data_out:
            data_out.write(self.last_response)
            data_out.write("\n")

    def do_responseReformatJson(self, args):
        try:
            _ = json.loads(self.last_response)
        except (json.decoder.JSONDecodeError, TypeError):
            print(colorize_msg("The last response isn't JSON!", "warning"))
            return

        self.json_output_format = (
            "json" if self.json_output_format == "jsonl" else "jsonl"
        )
        self.print_with_new_lines(self.last_response, "B")

    def do_restart(self, arg):
        self.restart = True
        return True

    def do_restartDebug(self, arg):
        self.restart_debug = True
        return True

    @cmd_decorator()
    def do_setOutputColor(self, **kwargs):
        """
        Turns on/off adding colors to JSON responses

        Syntax:
            setOutputColor {on|off}
        """

        if not kwargs["parsed_args"].output_color:
            self.print_response(
                colorize_msg(
                    "Output colored responses is"
                    f" {'on' if self.json_output_color else 'off'}",
                    "info",
                )
            )
            return

        if kwargs["parsed_args"].output_color.lower() not in ("on", "off"):
            self.print_response(
                colorize_msg("Color mode should be on or off", "warning")
            )
            return

        if kwargs["parsed_args"].output_color.lower() == "on":
            self.json_output_color = True
            self.print_response(colorize_msg("Colored output is enabled", "info"))

        if kwargs["parsed_args"].output_color.lower() == "off":
            self.json_output_color = False
            self.print_response(colorize_msg("Colored output is disabled", "info"))

        self.write_config()

    @cmd_decorator()
    def do_setOutputFormat(self, **kwargs):
        """
        Set output format for JSON responses

        Syntax:
            setOutputFormat {jsonl|json}
        """

        if not kwargs["parsed_args"].output_format:
            self.print_response(
                colorize_msg(f"Current format is {self.json_output_format}", "info")
            )
            return

        if kwargs["parsed_args"].output_format.lower() not in ("json", "jsonl"):
            self.print_response(
                colorize_msg(
                    "Format should be json (tall json) or jsonl (json line)", "warning"
                )
            )
            return

        self.print_response(
            colorize_msg(
                f"JSON format set to {kwargs['parsed_args'].output_format.lower()}",
                "info",
            )
        )

        self.json_output_format = kwargs["parsed_args"].output_format.lower()
        self.write_config()

    @cmd_decorator()
    def do_setTheme(self, **kwargs):
        """
        Switch terminal ANSI colors between default and light

        Syntax:
            setTheme {default|light}
        """
        Colors.set_theme(kwargs["parsed_args"].theme[0])
        print()

    def do_timer(self, arg):
        if self.timer_on:
            self.timer_on = False
            self.print_response("Timer is off", "success")
        else:
            self.timer_on = True
            self.print_response("Timer is on", "success")

    # Support methods

    def get_restart(self):
        return self.restart

    def get_restart_debug(self):
        return self.restart_debug

    def parse(self, argument_string):
        """Parses command arguments into a list of argument strings"""

        try:
            shlex_list = shlex.split(argument_string)
            return shlex_list
        except ValueError as err:
            self.print_error(err, "Unable to parse arguments")
            raise

    def print_with_new_lines(self, ln, pos=""):
        def add_color(str_to_color):
            if self.json_output_color and not cli_args.colorDisable:
                return colorize_json(str_to_color)
            return str_to_color

        pos = pos.upper()
        if orjson_avail:
            try:
                # Test if data is json and format appropriately
                _ = orjson.loads(ln)
            except (orjson.JSONDecodeError, TypeError):
                output = ln
            else:
                if type(ln) not in [dict, list]:
                    ln = orjson.loads(ln)
                if self.json_output_format == "json" and not cli_args.formatDisable:
                    json_str = orjson.dumps(ln, option=orjson.OPT_INDENT_2)
                else:
                    json_str = orjson.dumps(ln)

                output = add_color(json_str.decode())
        else:
            try:
                _ = json.loads(ln)
            except (json.decoder.JSONDecodeError, TypeError):
                output = ln
            else:
                if type(ln) not in [dict, list]:
                    ln = json.loads(ln)
                if self.json_output_format == "json" and not cli_args.formatDisable:
                    json_str = json.dumps(ln, indent=2)
                else:
                    json_str = json.dumps(ln)

                output = add_color(json_str)

        if pos == "S" or pos == "START":
            print(f"\n{output}", flush=True)
        elif pos == "E" or pos == "END":
            print(f"{output}\n", flush=True)
        elif pos == "B" or pos == "BOTH":
            print(f"\n{output}\n", flush=True)
        else:
            print(f"{output}", flush=True)

        # Capture the latest output to send to clipboard or file, removing color codes
        self.last_response = re.sub(r"(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]", "", output)

    def print_error(self, err, msg=""):
        self.print_with_new_lines(
            colorize_msg(f'ERROR: {msg}{" : " if msg else ""}{err}', "error"), "B"
        )

    def print_response(self, response, color=""):
        if response:
            self.print_with_new_lines(colorize_msg(response, color), "B")
        else:
            self.print_with_new_lines(colorize_msg("No response!", "info"), "B")

    def write_config(self):
        if not self.docker_launched:
            self.config["FORMATTING"] = {
                "JsonFormat": self.json_output_format,
                "ColorOutput": f'{"True" if self.json_output_color else "False"}',
            }
            try:
                with open(self.config_file, "w") as config_file:
                    self.config.write(config_file)
            except IOError as ex:
                if self.config_error == 0:
                    self.print_response(
                        colorize_msg(
                            "Error writing the config file, configuration cannot be"
                            f" saved (this warning will not repeat): {ex}"
                        ),
                        "warning",
                    )
                    self.config_error += 1
            except configparser.Error as ex:
                if self.config_error == 0:
                    self.print_response(
                        colorize_msg(
                            "Error writing entries to the config file, configuration"
                            f" cannot be saved (this warning with not repeat): {ex}"
                        ),
                        "warning",
                    )
                    self.config_error += 1

    # ===== Auto completers =====

    # TODO Order
    def complete_addRecord(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_deleteRecord(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_exportCSVEntityReport(self, text, line, begidx, endidx):
        if re.match("exportCSVEntityReport +", line) and not re.match(
            "exportCSVEntityReport +.* +", line
        ):
            return self.path_completes(
                text, line, begidx, endidx, "exportCSVEntityReport"
            )

        if re.match(".* -f +", line):
            return self.flags_completes(text, line)

    def complete_exportJSONEntityReport(self, text, line, begidx, endidx):
        if re.match("exportJSONEntityReport +", line) and not re.match(
            "exportJSONEntityReport +.* +", line
        ):
            return self.path_completes(
                text, line, begidx, endidx, "exportJSONEntityReport"
            )

        if re.match(".* -f +", line):
            return self.flags_completes(text, line)

    def complete_findInterestingEntitiesByEntityID(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_findInterestingEntitiesByRecordID(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_findNetworkByEntityID(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_findNetworkByRecordID(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_findPathByEntityID(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_findPathByRecordID(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_getEntityByEntityID(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_getEntityByRecordID(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_getRecord(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_getVirtualEntityByRecordID(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_howEntityByEntityID(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_processRedoRecord(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_reevaluateEntity(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_reevaluateRecord(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_replaceRecord(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_searchByAttributes(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def complete_whyRecordInEntity(self, text, line, begidx, endidx):
        return self.flags_completes(text, line)

    def flags_completes(self, text, line):
        """Auto complete engine flags from szengineflags"""
        if re.match(".* -f +", line):
            return [
                flag
                for flag in self.engine_flags_list
                if flag.lower().startswith(text.lower())
            ]
        return None

    @staticmethod
    def path_completes(text, line, begidx, endidx, callingcmd):
        """Auto complete paths for commands"""

        completes = []
        path_comp = line[len(callingcmd) + 1 : endidx]
        fixed = line[len(callingcmd) + 1 : begidx]
        for path in glob.glob(f"{path_comp}*"):
            path = (
                path + os.sep
                if path and os.path.isdir(path) and path[-1] != os.sep
                else path
            )
            completes.append(path.replace(fixed, "", 1))

        return completes

    def complete_addConfigFile(self, text, line, begidx, endidx):
        if re.match("addConfigFile +", line):
            return self.path_completes(text, line, begidx, endidx, "addConfigFile")

    def complete_processFile(self, text, line, begidx, endidx):
        if re.match("processFile +", line):
            return self.path_completes(text, line, begidx, endidx, "processFile")

    def complete_responseToFile(self, text, line, begidx, endidx):
        if re.match("responseToFile +", line):
            return self.path_completes(text, line, begidx, endidx, "responseToFile")

    def complete_setOutputColor(self, text, line, begidx, endidx):
        if re.match("setOutputColor +", line):
            options = ["on", "off"]
            return [
                option for option in options if option.lower().startswith(text.lower())
            ]
        return None

    def complete_setOutputFormat(self, text, line, begidx, endidx):
        if re.match("setOutputFormat +", line):
            options = ["json", "jsonl"]
            return [
                option for option in options if option.lower().startswith(text.lower())
            ]
        return None


# ---- Utility functions ----


def colorize(in_string, color_list="None"):
    return Colors.apply(in_string, color_list)


def colorize_json(json_str):
    key_replacer = rf"\1{Colors.FG_LIGHTBLUE}\2{Colors.RESET}\3\4"
    value_replacer = rf"\1\2{Colors.FG_YELLOW}\3{Colors.RESET}\4\5"
    # Look for values first to make regex a little easier to construct
    # Regex is matching: ': "Robert Smith", ' and using the groups in the replacer to add color
    json_color = re.sub(
        r"(: ?)(\")([\w\/+][^\{\"]+?)(\")(\}?|,{1}|\n)", value_replacer, json_str
    )
    # Regex is matching: ': "ENTITY_ID": ' and using the groups in the replacer to add color
    json_color = re.sub(r"(\")([\w ]*?)(\")(:{1})", key_replacer, json_color)
    return json_color


def colorize_msg(msg_text, msg_type_or_color=""):

    if cli_args.colorDisable:
        return msg_text

    if msg_type_or_color.upper() == "ERROR":
        msg_color = "bad"
    elif msg_type_or_color.upper() == "WARNING":
        msg_color = "caution,italics"
    elif msg_type_or_color.upper() == "INFO":
        msg_color = "highlight2"
    elif msg_type_or_color.upper() == "SUCCESS":
        msg_color = "good"
    else:
        msg_color = msg_type_or_color
    return f"{Colors.apply(msg_text, msg_color)}"


def get_engine_flags(flags_list):
    """Detect if int or named flags are used and convert to int ready to send to API call"""

    # For Senzing support team
    if flags_list[0] == "-1":
        return -1

    # An int is used for the engine flags - old method still support
    if len(flags_list) == 1 and flags_list[0].isnumeric():
        return int(flags_list[0])

    # Named engine flag(s) were used, combine when > 1
    try:
        engine_flags = SzEngineFlags.combine_flags(flags_list)
    except KeyError as err:
        raise KeyError(f"Invalid engine flag: {err}") from err

    return engine_flags


if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        "fileToProcess",
        default=None,
        help=textwrap.dedent(
            """\
            
            Path and file name of file with commands to process.
        
        """
        ),
        nargs="?",
    )
    parser.add_argument(
        "-c",
        "--iniFile",
        default="",
        help=textwrap.dedent(
            """\
            
            Path and file name of optional G2Module.ini to use.
        
        """
        ),
        nargs=1,
    )
    parser.add_argument(
        "-t",
        "--debugTrace",
        action="store_true",
        default=False,
        help=textwrap.dedent(
            """\
            
            Output debug information.
        
        """
        ),
    )
    parser.add_argument(
        "-H",
        "--hist_disable",
        action="store_true",
        default=False,
        help=textwrap.dedent(
            """\
            
            Disable history file usage.
        
        """
        ),
    )
    parser.add_argument(
        "-C",
        "--colorDisable",
        action="store_true",
        default=False,
        help=textwrap.dedent(
            """\
            
            Disable coloring of output for the session, color formatting commands will have no effect in the session.
        
        """
        ),
    )
    parser.add_argument(
        "-F",
        "--formatDisable",
        action="store_true",
        default=False,
        help=textwrap.dedent(
            """\
            
            Disable formatting of JSON output for the session, JSON formatting commands will have no effect in the session.
        
        """
        ),
    )
    cli_args = parser.parse_args()

    first_loop = True
    restart = False

    # Check if INI file or env var is specified, otherwise use default INI file
    # ini_file_name = None

    # if cli_args.iniFile:
    #     ini_file_name = pathlib.Path(cli_args.iniFile[0])
    # elif os.getenv("SENZING_ENGINE_CONFIGURATION_JSON"):
    #     g2module_params = os.getenv("SENZING_ENGINE_CONFIGURATION_JSON")
    # else:
    #     ini_file_name = pathlib.Path(G2Paths.get_G2Module_ini_path())

    # if ini_file_name:
    #     G2Paths.check_file_exists_and_readable(ini_file_name)
    #     iniParamCreator = G2IniParams()
    #     g2module_params = iniParamCreator.getJsonINIParams(ini_file_name)

    # TODO REmove when have new tools helpers
    secj = os.environ.get("SENZING_ENGINE_CONFIGURATION_JSON")
    if not secj or (secj and len(secj) == 0):
        print(
            "\nERROR: SENZING_ENGINE_CONFIGURATION_JSON environment variable is not set"
        )
        sys.exit(1)

    # Execute a file of commands
    if cli_args.fileToProcess:
        cmd_obj = SzCmdShell(secj, cli_args.debugTrace, cli_args.hist_disable)
        cmd_obj.fileloop(cli_args.fileToProcess)
    # Start command shell
    else:
        # Don't use args.debugTrace here, may need to restart
        debug_trace = cli_args.debugTrace

        while first_loop or restart:
            # Have we been in the command shell already and are trying to quit? Used for restarting
            if "cmd_obj" in locals() and cmd_obj.ret_quit():
                break

            cmd_obj = SzCmdShell(secj, debug_trace, cli_args.hist_disable)
            cmd_obj.cmdloop()

            restart = (
                True if cmd_obj.get_restart() or cmd_obj.get_restart_debug() else False
            )
            debug_trace = True if cmd_obj.get_restart_debug() else False
            first_loop = False
