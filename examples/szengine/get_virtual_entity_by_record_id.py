from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
try:
    flags = SzEngineFlags.SZ_VIRTUAL_ENTITY_DEFAULT_FLAGS
    record_list = [
        ("CUSTOMERS", "1001"),
        ("CUSTOMERS", "1002"),
    ]
    result = sz_engine.get_virtual_entity_by_record_id(record_list, flags)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
