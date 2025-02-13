from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
try:
    BUILD_OUT_DEGREES = 1
    FLAGS = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS
    MAX_DEGREES = 2
    MAX_ENTITIES = 10
    RECORD_LIST = [("CUSTOMERS", "1001"), ("CUSTOMERS", "1009")]
    RESULT = sz_engine.find_network_by_record_id(RECORD_LIST, MAX_DEGREES, BUILD_OUT_DEGREES, MAX_ENTITIES, FLAGS)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
