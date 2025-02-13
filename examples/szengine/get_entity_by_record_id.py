from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
try:
    DATA_SOURCE_CODE = "CUSTOMERS"
    flags = SzEngineFlags.SZ_ENTITY_DEFAULT_FLAGS
    RECORD_ID = "1001"
    result = sz_engine.get_entity_by_record_id(DATA_SOURCE_CODE, RECORD_ID, flags)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
