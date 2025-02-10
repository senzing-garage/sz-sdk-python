#! /usr/bin/env python3
from senzing import SzError

from .setup_senzing import get_sz_abstract_factory

try:
    sz_abstract_factory = get_sz_abstract_factory()
    sz_configmanager = sz_abstract_factory.create_configmanager()
except SzError as err:
    print(f"\nERROR: {err}\n")
