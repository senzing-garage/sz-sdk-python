#! /usr/bin/env python3
from senzing import SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
try:
    sz_engine.prime_engine()
except SzError as err:
    print(f"\nERROR: {err}\n")
