from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
ENTITY_ID_1 = 1
ENTITY_ID_2 = 4
FLAGS = SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS
try:
    RESULT = sz_engine.why_entities(
        ENTITY_ID_1,
        ENTITY_ID_2,
        FLAGS,
    )
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
