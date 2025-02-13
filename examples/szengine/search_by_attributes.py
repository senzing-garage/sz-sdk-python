import json

from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
ATTRIBUTES = json.dumps({"NAME_FULL": "BOB SMITH", "EMAIL_ADDRESS": "bsmith@work.com"})
FLAGS = SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS
SEARCH_PROFILE = ""
try:
    RESULT = sz_engine.search_by_attributes(ATTRIBUTES, FLAGS, SEARCH_PROFILE)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
