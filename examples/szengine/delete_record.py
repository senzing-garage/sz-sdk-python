#! /usr/bin/env python3
from senzing import SzEngineFlags, SzError

from . import get_sz_engine

DATA_SOURCE_CODE = "TEST"
FLAGS = SzEngineFlags.SZ_WITH_INFO
RECORD_ID = "1"
try:
    sz_engine = get_sz_engine()
    RESULT = sz_engine.delete_record(DATA_SOURCE_CODE, RECORD_ID, FLAGS)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
