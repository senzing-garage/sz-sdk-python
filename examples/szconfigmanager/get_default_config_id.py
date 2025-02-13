from senzing import SzError

from . import get_sz_configmanager

sz_configmanager = get_sz_configmanager()
try:
    CONFIG_ID = sz_configmanager.get_default_config_id()
    print(f"\n{CONFIG_ID}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
