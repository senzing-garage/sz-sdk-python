from senzing import SzEngineFlags, SzError

from . import sz_engine

try:
    DATA_SOURCE_CODE = "CUSTOMERS"
    flags = SzEngineFlags.SZ_RECORD_DEFAULT_FLAGS
    RECORD_ID = "1001"
    result = sz_engine.get_record(DATA_SOURCE_CODE, RECORD_ID, flags)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
