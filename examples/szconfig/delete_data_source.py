#! /usr/bin/env python3
from senzing import SzError

from .setup_senzing import get_sz_abstract_factory

DATA_SOURCE_CODE = "TEST"
try:
    sz_abstract_factory = get_sz_abstract_factory()
    sz_config = sz_abstract_factory.create_config()
    config_handle = sz_config.create_config()
    sz_config.delete_data_source(config_handle, DATA_SOURCE_CODE)
    sz_config.close_config(config_handle)
except SzError as err:
    print(f"\nERROR: {err}\n")
