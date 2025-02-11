#! /usr/bin/env python3
from senzing import SzEngineFlags, SzError

from . import get_sz_engine

DATA_SOURCE_CODE = "CUSTOMERS"
FLAGS = SzEngineFlags.SZ_WHY_RECORDS_DEFAULT_FLAGS
RECORD_ID = "1001"
try:
    sz_engine = get_sz_engine()
    RESULT = sz_engine.why_record_in_entity(
        DATA_SOURCE_CODE,
        RECORD_ID,
        FLAGS,
    )
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
