from typing import List

from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
try:
    avoid_entity_ids: List[int] = []
    END_ENTITY_ID = 4
    flags = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS
    MAX_DEGREES = 2
    required_data_sources: List[str] = []
    START_ENTITY_ID = 1
    result = sz_engine.find_path_by_entity_id(
        START_ENTITY_ID,
        END_ENTITY_ID,
        MAX_DEGREES,
        avoid_entity_ids,
        required_data_sources,
        flags,
    )
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
