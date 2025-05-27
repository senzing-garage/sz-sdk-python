from senzing import SzEngineFlags, SzError

from . import sz_engine

entity_id = 1
flags = SzEngineFlags.SZ_ENTITY_DEFAULT_FLAGS

try:
    result = sz_engine.get_entity_by_entity_id(entity_id, flags)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
