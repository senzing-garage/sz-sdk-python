from typing import List, Tuple

from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
AVOID_RECORD_KEYS: List[Tuple[str, str]] = []
END_DATA_SOURCE_CODE = "CUSTOMERS"
END_RECORD_ID = "1009"
FLAGS = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS
MAX_DEGREES = 2
REQUIRED_DATA_SOURCES: List[str] = []
START_DATA_SOURCE_CODE = "CUSTOMERS"
START_RECORD_ID = "1001"
try:
    RESULT = sz_engine.find_path_by_record_id(
        START_DATA_SOURCE_CODE,
        START_RECORD_ID,
        END_DATA_SOURCE_CODE,
        END_RECORD_ID,
        MAX_DEGREES,
        AVOID_RECORD_KEYS,
        REQUIRED_DATA_SOURCES,
        FLAGS,
    )
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
