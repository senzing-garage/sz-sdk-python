from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
DATA_SOURCE_CODE = "CUSTOMERS"
FLAGS = SzEngineFlags.SZ_ENTITY_DEFAULT_FLAGS
RECORD_ID = "1001"
try:
    RESULT = sz_engine.get_entity_by_record_id(DATA_SOURCE_CODE, RECORD_ID, FLAGS)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
