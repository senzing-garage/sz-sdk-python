#! /usr/bin/env python3
from senzing import SzError

from setup_senzing import get_sz_abstract_factory

try:
    sz_abstract_factory = get_sz_abstract_factory()
    sz_product = sz_abstract_factory.create_product()
    RESULT = sz_product.get_version()
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
