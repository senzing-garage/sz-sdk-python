#! /usr/bin/env python3
from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
FLAGS = SzEngineFlags.SZ_VIRTUAL_ENTITY_DEFAULT_FLAGS
RECORD_LIST = [
    ("CUSTOMERS", "1001"),
    ("CUSTOMERS", "1002"),
]
try:
    RESULT = sz_engine.get_virtual_entity_by_record_id(RECORD_LIST, FLAGS)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
