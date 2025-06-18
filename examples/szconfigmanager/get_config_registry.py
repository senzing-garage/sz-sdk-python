from senzing import SzError

from . import sz_configmanager

try:
    config_list = sz_configmanager.get_config_registry()
    print(f"\n{config_list}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
