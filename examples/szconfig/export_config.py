#! /usr/bin/env python3
from senzing import SzError

from . import get_sz_config

try:
    sz_config = get_sz_config()
    config_handle = sz_config.create_config()  # Create first in-memory.
    CONFIG_DEFINITION = sz_config.export_config(config_handle)  # Save in-memory to string.
    sz_config.close_config(config_handle)
    print(f"\n{CONFIG_DEFINITION}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
