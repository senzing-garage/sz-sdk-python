from senzing import SzError

from . import get_sz_configmanager

sz_configmanager = get_sz_configmanager()
try:
    CONFIG_LIST = sz_configmanager.get_configs()
    print(f"\n{CONFIG_LIST}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
