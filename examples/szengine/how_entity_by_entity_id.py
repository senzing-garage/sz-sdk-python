from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
try:
    ENTITY_ID = 1
    flags = SzEngineFlags.SZ_HOW_ENTITY_DEFAULT_FLAGS
    result = sz_engine.how_entity_by_entity_id(ENTITY_ID, flags)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
