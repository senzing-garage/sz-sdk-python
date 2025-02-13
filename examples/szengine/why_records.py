from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
try:
    DATA_SOURCE_CODE_1 = "CUSTOMERS"
    DATA_SOURCE_CODE_2 = "CUSTOMERS"
    flags = SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS
    RECORD_ID_1 = "1001"
    RECORD_ID_2 = "1002"
    result = sz_engine.why_records(
        DATA_SOURCE_CODE_1,
        RECORD_ID_1,
        DATA_SOURCE_CODE_2,
        RECORD_ID_2,
        flags,
    )
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
