from senzing import SzEngineFlags, SzError

from . import sz_engine

try:
    DATA_SOURCE_CODE = "TEST"
    flags = SzEngineFlags.SZ_WITH_INFO
    RECORD_ID = "1"
    RESULT = sz_engine.delete_record(DATA_SOURCE_CODE, RECORD_ID, flags)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
