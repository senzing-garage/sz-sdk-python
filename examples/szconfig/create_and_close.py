#! /usr/bin/env python3
from senzing import SzError

from . import get_sz_config

try:
    sz_config = get_sz_config()
    config_handle = sz_config.create_config()

    # Do work.

    sz_config.close_config(config_handle)
except SzError as err:
    print(f"\nERROR: {err}\n")
