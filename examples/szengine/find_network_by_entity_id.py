#! /usr/bin/env python3
from senzing import SzEngineFlags, SzError

from . import get_sz_abstract_factory

BUILD_OUT_DEGREES = 1
ENTITY_LIST = [1, 4]
FLAGS = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS
MAX_DEGREES = 2
MAX_ENTITIES = 10
try:
    sz_abstract_factory = get_sz_abstract_factory()
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.find_network_by_entity_id(ENTITY_LIST, MAX_DEGREES, BUILD_OUT_DEGREES, MAX_ENTITIES, FLAGS)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
