from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
try:
    BUILD_OUT_DEGREES = 1
    flags = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS
    MAX_DEGREES = 2
    MAX_ENTITIES = 10
    record_list = [("CUSTOMERS", "1001"), ("CUSTOMERS", "1009")]
    result = sz_engine.find_network_by_record_id(record_list, MAX_DEGREES, BUILD_OUT_DEGREES, MAX_ENTITIES, flags)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
