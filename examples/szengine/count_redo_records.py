#! /usr/bin/env python3
from senzing import SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
try:
    RESULT = sz_engine.count_redo_records()
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
