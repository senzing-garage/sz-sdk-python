import json

from senzing import SzEngineFlags, SzError

from . import sz_engine

try:
    attributes = json.dumps({"NAME_FULL": "BOB SMITH", "EMAIL_ADDRESS": "bsmith@work.com"})
    ENTITY_ID = 1
    flags = SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS
    SEARCH_PROFILE = "SEARCH"
    RESULT = sz_engine.why_search(attributes, ENTITY_ID, flags, SEARCH_PROFILE)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
