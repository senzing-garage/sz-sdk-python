from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
try:
    ENTITY_ID = 1
    FLAGS = SzEngineFlags.SZ_WITH_INFO
    RESULT = sz_engine.reevaluate_entity(ENTITY_ID, FLAGS)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
