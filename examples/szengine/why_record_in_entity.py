from senzing import SzEngineFlags, SzError

from . import sz_engine

try:
    DATA_SOURCE_CODE = "CUSTOMERS"
    flags = SzEngineFlags.SZ_WHY_RECORDS_DEFAULT_FLAGS
    RECORD_ID = "1001"
    RESULT = sz_engine.why_record_in_entity(
        DATA_SOURCE_CODE,
        RECORD_ID,
        flags,
    )
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
