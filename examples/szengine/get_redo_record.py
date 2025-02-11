#! /usr/bin/env python3
from senzing import SzError

from . import get_sz_engine

try:
    sz_engine = get_sz_engine()
    RESULT = sz_engine.get_redo_record()
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
