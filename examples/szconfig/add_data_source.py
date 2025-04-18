from senzing import SzError

from . import sz_configmanager

try:
    DATA_SOURCE_CODE = "NAME_OF_DATASOURCE"
    sz_config = sz_configmanager.create_config_from_template()
    result = sz_config.add_data_source(DATA_SOURCE_CODE)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
