#! /usr/bin/env python3
from typing import List

from senzing import SzEngineFlags, SzError

from . import get_sz_engine

AVOID_ENTITY_IDS: List[int] = []
END_ENTITY_ID = 4
FLAGS = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS
MAX_DEGREES = 2
REQUIRED_DATA_SOURCES: List[str] = []
START_ENTITY_ID = 1
try:
    sz_engine = get_sz_engine()
    RESULT = sz_engine.find_path_by_entity_id(
        START_ENTITY_ID,
        END_ENTITY_ID,
        MAX_DEGREES,
        AVOID_ENTITY_IDS,
        REQUIRED_DATA_SOURCES,
        FLAGS,
    )
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
