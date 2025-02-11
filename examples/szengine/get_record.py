#! /usr/bin/env python3
from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
DATA_SOURCE_CODE = "CUSTOMERS"
FLAGS = SzEngineFlags.SZ_RECORD_DEFAULT_FLAGS
RECORD_ID = "1001"
try:
    RESULT = sz_engine.get_record(DATA_SOURCE_CODE, RECORD_ID, FLAGS)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
