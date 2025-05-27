from typing import List

from senzing import SzEngineFlags, SzError

from . import sz_engine

avoid_entity_ids: List[int] = []
end_entity_id = 400215
flags = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS
max_degrees = 2
required_data_sources: List[str] = []
start_entity_id = 1

try:
    result = sz_engine.find_path_by_entity_id(
        start_entity_id,
        end_entity_id,
        max_degrees,
        avoid_entity_ids,
        required_data_sources,
        flags,
    )
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
