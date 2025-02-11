#! /usr/bin/env python3
from senzing import SzEngineFlags, SzError

from . import get_sz_engine

ENTITY_ID = 1
FLAGS = SzEngineFlags.SZ_HOW_ENTITY_DEFAULT_FLAGS
try:
    sz_engine = get_sz_engine()
    RESULT = sz_engine.how_entity_by_entity_id(ENTITY_ID, FLAGS)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
