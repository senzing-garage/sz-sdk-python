from senzing import SzError

from . import get_sz_config

sz_config = get_sz_config()
try:
    DATA_SOURCE_CODE = "TEST"
    config_handle = sz_config.create_config()
    sz_config.delete_data_source(config_handle, DATA_SOURCE_CODE)
    sz_config.close_config(config_handle)
except SzError as err:
    print(f"\nERROR: {err}\n")
