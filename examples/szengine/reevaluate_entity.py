from senzing import SzEngineFlags, SzError

from . import sz_engine

entity_id = 1
flags = SzEngineFlags.SZ_WITH_INFO

try:
    result = sz_engine.reevaluate_entity(entity_id, flags)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
