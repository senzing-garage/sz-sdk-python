from senzing import SzEngineFlags, SzError

from . import sz_engine

data_source_code = "CUSTOMERS"
flags = SzEngineFlags.SZ_WHY_RECORDS_DEFAULT_FLAGS
record_id = "1001"

try:
    result = sz_engine.why_record_in_entity(
        data_source_code,
        record_id,
        flags,
    )
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
