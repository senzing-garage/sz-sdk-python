#! /usr/bin/env python3
from senzing import SzEngineFlags, SzError

from .setup_senzing import get_sz_abstract_factory

DATA_SOURCE_CODE = "CUSTOMERS"
FLAGS = SzEngineFlags.SZ_WITH_INFO
RECORD_ID = "1001"
try:
    sz_abstract_factory = get_sz_abstract_factory()
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.reevaluate_record(DATA_SOURCE_CODE, RECORD_ID, FLAGS)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
