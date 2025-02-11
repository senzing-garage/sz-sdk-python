#! /usr/bin/env python3
from senzing import SzError

from . import get_sz_product

try:
    sz_product = get_sz_product()
    RESULT = sz_product.get_version()
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
