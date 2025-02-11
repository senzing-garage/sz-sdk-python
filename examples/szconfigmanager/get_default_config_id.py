#! /usr/bin/env python3
from senzing import SzError

from . import get_sz_configmanager

try:
    sz_configmanager = get_sz_configmanager()
    CONFIG_ID = sz_configmanager.get_default_config_id()
    print(f"\n{CONFIG_ID}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
