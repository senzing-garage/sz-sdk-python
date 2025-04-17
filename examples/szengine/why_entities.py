from senzing import SzEngineFlags, SzError

from . import sz_engine

try:
    ENTITY_ID_1 = 1
    ENTITY_ID_2 = 4
    flags = SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS
    RESULT = sz_engine.why_entities(
        ENTITY_ID_1,
        ENTITY_ID_2,
        flags,
    )
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
