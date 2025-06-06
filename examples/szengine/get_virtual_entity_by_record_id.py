from senzing import SzEngineFlags, SzError

from . import sz_engine

flags = SzEngineFlags.SZ_VIRTUAL_ENTITY_DEFAULT_FLAGS
record_list = [
    ("CUSTOMERS", "1001"),
    ("CUSTOMERS", "1002"),
]

try:
    result = sz_engine.get_virtual_entity_by_record_id(record_list, flags)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
