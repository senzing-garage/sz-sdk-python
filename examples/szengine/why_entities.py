#! /usr/bin/env python3
from senzing import SzEngineFlags, SzError

from .setup_senzing import get_sz_abstract_factory

ENTITY_ID_1 = 1
ENTITY_ID_2 = 4
FLAGS = SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS
try:
    sz_abstract_factory = get_sz_abstract_factory()
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.why_entities(
        ENTITY_ID_1,
        ENTITY_ID_2,
        FLAGS,
    )
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
