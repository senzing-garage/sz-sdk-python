#! /usr/bin/env python3
from senzing import SzError

from .setup_senzing import get_sz_abstract_factory

try:
    sz_abstract_factory = get_sz_abstract_factory()
    sz_engine = sz_abstract_factory.create_engine()
except SzError as err:
    print(f"\nERROR: {err}\n")
