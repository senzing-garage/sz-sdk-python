#! /usr/bin/env python3
from senzing import SzError

from . import get_sz_abstract_factory

try:
    sz_abstract_factory = get_sz_abstract_factory()
    sz_config = sz_abstract_factory.create_config()
    config_handle = sz_config.create_config()

    # Do work.

    sz_config.close_config(config_handle)
except SzError as err:
    print(f"\nERROR: {err}\n")
