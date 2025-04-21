import json

from senzing import SzError

from . import sz_configmanager

try:
    config_definition = json.dumps({})
    sz_config = sz_configmanager.create_config_from_string(config_definition)
except SzError as err:
    print(f"\nERROR: {err}\n")
