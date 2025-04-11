from senzing import SzError

from . import sz_configmanager

try:
    sz_config = sz_configmanager.create_config_from_template()
    CONFIG_DEFINITION = sz_config.export()
    print(f"\n{CONFIG_DEFINITION}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
