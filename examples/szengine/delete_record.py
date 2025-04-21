from senzing import SzEngineFlags, SzError

from . import sz_engine

data_source_code = "TEST"
flags = SzEngineFlags.SZ_WITH_INFO
record_id = "1"

try:
    result = sz_engine.delete_record(data_source_code, record_id, flags)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
