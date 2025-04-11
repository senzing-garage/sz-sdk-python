from senzing import SzEngineFlags, SzError

from . import sz_engine

try:
    ENTITY_ID = 1
    flags = SzEngineFlags.SZ_WITH_INFO
    RESULT = sz_engine.reevaluate_entity(ENTITY_ID, flags)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
