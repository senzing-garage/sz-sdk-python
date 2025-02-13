from senzing import SzError

from . import get_sz_config

sz_config = get_sz_config()
try:
    config_handle = sz_config.create_config()  # Create first in-memory.
    config_definition = sz_config.export_config(config_handle)  # Save in-memory to string.
    sz_config.close_config(config_handle)
    print(f"\n{config_definition}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
