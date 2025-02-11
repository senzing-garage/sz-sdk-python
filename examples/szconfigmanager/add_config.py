#! /usr/bin/env python3
from senzing import SzError

from . import get_sz_abstract_factory

sz_abstract_factory = get_sz_abstract_factory()
CONFIG_COMMENT = "Just an empty example"
try:
    sz_config = sz_abstract_factory.create_config()
    sz_configmanager = sz_abstract_factory.create_configmanager()
    config_handle = sz_config.create_config()
    CONFIG_DEFINITION = sz_config.export_config(config_handle)
    config_id = sz_configmanager.add_config(CONFIG_DEFINITION, CONFIG_COMMENT)
except SzError as err:
    print(f"\nERROR: {err}\n")
