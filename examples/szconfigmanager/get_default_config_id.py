from senzing import SzError

from . import sz_configmanager

try:
    config_id = sz_configmanager.get_default_config_id()
    print(f"\n{config_id}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
