from senzing import SzError

from . import get_sz_config

sz_config = get_sz_config()
DATA_SOURCE_CODE = "NAME_OF_DATASOURCE"
try:
    config_handle = sz_config.create_config()
    RESULT = sz_config.add_data_source(config_handle, DATA_SOURCE_CODE)
    sz_config.close_config(config_handle)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
