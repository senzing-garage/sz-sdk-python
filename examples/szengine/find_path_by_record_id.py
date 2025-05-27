from typing import List, Tuple

from senzing import SzEngineFlags, SzError

from . import sz_engine

avoid_record_keys: List[Tuple[str, str]] = []
end_data_source_code = "WATCHLIST"
end_record_id = "1007"
flags = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS
max_degrees = 2
required_data_sources: List[str] = []
start_data_source_code = "CUSTOMERS"
start_record_id = "1001"

try:
    result = sz_engine.find_path_by_record_id(
        start_data_source_code,
        start_record_id,
        end_data_source_code,
        end_record_id,
        max_degrees,
        avoid_record_keys,
        required_data_sources,
        flags,
    )
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
