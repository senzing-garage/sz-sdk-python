from senzing import SzError

from . import get_sz_config

sz_config = get_sz_config()
try:
    config_handle_1 = sz_config.create_config()  # Create first in-memory.
    CONFIG_DEFINITION = sz_config.export_config(config_handle_1)  # Save in-memory to string.
    config_handle_2 = sz_config.import_config(CONFIG_DEFINITION)  # Create second in-memory.
    sz_config.close_config(config_handle_1)
    sz_config.close_config(config_handle_2)
except SzError as err:
    print(f"\nERROR: {err}\n")
