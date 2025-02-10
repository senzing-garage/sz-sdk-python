#! /usr/bin/env python3
from senzing import SzEngineFlags, SzError

from .setup_senzing import get_sz_abstract_factory

DATA_SOURCE_CODE_1 = "CUSTOMERS"
DATA_SOURCE_CODE_2 = "CUSTOMERS"
FLAGS = SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS
RECORD_ID_1 = "1001"
RECORD_ID_2 = "1002"
try:
    sz_abstract_factory = get_sz_abstract_factory()
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.why_records(
        DATA_SOURCE_CODE_1,
        RECORD_ID_1,
        DATA_SOURCE_CODE_2,
        RECORD_ID_2,
        FLAGS,
    )
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
