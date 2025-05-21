from senzing import SzEngineFlags, SzError

from . import sz_engine

data_source_code_1 = "CUSTOMERS"
data_source_code_2 = "CUSTOMERS"
flags = SzEngineFlags.SZ_WHY_RECORDS_DEFAULT_FLAGS
record_id_1 = "1001"
record_id_2 = "1002"

try:
    result = sz_engine.why_records(
        data_source_code_1,
        record_id_1,
        data_source_code_2,
        record_id_2,
        flags,
    )
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
