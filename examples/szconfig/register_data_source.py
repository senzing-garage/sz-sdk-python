from senzing import SzError

from . import sz_configmanager

data_source_code = "NAME_OF_DATASOURCE"

try:
    sz_config = sz_configmanager.create_config_from_template()
    result = sz_config.register_data_source(data_source_code)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
