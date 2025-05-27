import json

from senzing import SzEngineFlags, SzError

from . import sz_engine

attributes = json.dumps({"NAME_FULL": "BOB SMITH", "EMAIL_ADDRESS": "bsmith@work.com"})
entity_id = 1
flags = SzEngineFlags.SZ_WHY_SEARCH_DEFAULT_FLAGS

try:
    result = sz_engine.why_search(attributes, entity_id, flags)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
