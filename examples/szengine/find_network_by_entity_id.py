from senzing import SzEngineFlags, SzError

from . import sz_engine

build_out_degrees = 1
entity_list = [1, 4]
flags = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS
max_degrees = 2
max_entities = 10

try:
    result = sz_engine.find_network_by_entity_id(entity_list, max_degrees, build_out_degrees, max_entities, flags)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
