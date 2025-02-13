from senzing import SzError

from . import get_sz_config

sz_config = get_sz_config()
try:
    config_handle = sz_config.create_config()
    result = sz_config.get_data_sources(config_handle)
    sz_config.close_config(config_handle)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
