from senzing import SzError

from . import sz_configmanager

try:
    sz_config = sz_configmanager.create_config_from_template()
    config_definition = sz_config.export()
    print(f"\n{config_definition}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
