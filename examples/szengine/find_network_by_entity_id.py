from senzing import SzEngineFlags, SzError

from . import sz_engine

try:
    BUILD_OUT_DEGREES = 1
    entity_list = [1, 4]
    flags = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS
    MAX_DEGREES = 2
    MAX_ENTITIES = 10
    RESULT = sz_engine.find_network_by_entity_id(entity_list, MAX_DEGREES, BUILD_OUT_DEGREES, MAX_ENTITIES, flags)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
