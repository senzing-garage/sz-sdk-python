from senzing import SzEngineFlags, SzError

from . import sz_engine

entity_id_1 = 1
entity_id_2 = 400215
flags = SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS

try:
    result = sz_engine.why_entities(
        entity_id_1,
        entity_id_2,
        flags,
    )
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
