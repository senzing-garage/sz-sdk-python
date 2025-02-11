#! /usr/bin/env python3
from senzing import SzError

from . import get_sz_abstract_factory

sz_abstract_factory = get_sz_abstract_factory()
try:
    sz_product = sz_abstract_factory.create_product()
except SzError as err:
    print(f"\nERROR: {err}\n")
