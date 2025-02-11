#! /usr/bin/env python3
from senzing import SzError

from . import get_sz_configmanager

sz_configmanager = get_sz_configmanager()
try:
    config_id = sz_configmanager.get_default_config_id()
    CONFIG_DEFINITION = sz_configmanager.get_config(config_id)
    print(f"\n{CONFIG_DEFINITION}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
