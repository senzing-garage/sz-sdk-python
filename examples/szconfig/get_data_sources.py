from senzing import SzError

from . import sz_configmanager

try:
    sz_config = sz_configmanager.create_config_from_template()
    result = sz_config.get_data_sources()
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
