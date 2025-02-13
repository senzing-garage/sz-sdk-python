from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
DATA_SOURCE_CODE = "CUSTOMERS"
FLAGS = SzEngineFlags.SZ_WITH_INFO
RECORD_ID = "1001"
try:
    RESULT = sz_engine.reevaluate_record(DATA_SOURCE_CODE, RECORD_ID, FLAGS)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
