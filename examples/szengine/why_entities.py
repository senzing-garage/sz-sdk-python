from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
try:
    ENTITY_ID_1 = 1
    ENTITY_ID_2 = 4
    flags = SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS
    result = sz_engine.why_entities(
        ENTITY_ID_1,
        ENTITY_ID_2,
        flags,
    )
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
