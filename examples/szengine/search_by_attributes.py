import json

from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
try:
    attributes = json.dumps({"NAME_FULL": "BOB SMITH", "EMAIL_ADDRESS": "bsmith@work.com"})
    flags = SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS
    SEARCH_PROFILE = ""
    result = sz_engine.search_by_attributes(attributes, flags, SEARCH_PROFILE)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
