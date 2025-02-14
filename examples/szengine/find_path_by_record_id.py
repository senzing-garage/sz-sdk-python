from typing import List, Tuple

from senzing import SzEngineFlags, SzError

from . import sz_engine

try:
    avoid_record_keys: List[Tuple[str, str]] = []
    END_DATA_SOURCE_CODE = "CUSTOMERS"
    END_RECORD_ID = "1009"
    flags = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS
    MAX_DEGREES = 2
    required_data_sources: List[str] = []
    START_DATA_SOURCE_CODE = "CUSTOMERS"
    START_RECORD_ID = "1001"
    result = sz_engine.find_path_by_record_id(
        START_DATA_SOURCE_CODE,
        START_RECORD_ID,
        END_DATA_SOURCE_CODE,
        END_RECORD_ID,
        MAX_DEGREES,
        avoid_record_keys,
        required_data_sources,
        flags,
    )
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
