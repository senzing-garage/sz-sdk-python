import time

from senzing import SzError

from . import sz_configmanager

try:
    sz_config = sz_configmanager.create_config_from_template()
    CURRENT_DEFAULT_CONFIG_ID = sz_configmanager.get_default_config_id()

    # Create a new config.

    sz_config = sz_configmanager.create_config_from_config_id(CURRENT_DEFAULT_CONFIG_ID)
    data_source_code = f"REPLACE_DEFAULT_CONFIG_ID_{time.time()}"
    sz_config.add_data_source(data_source_code)

    # Persist the new config.

    CONFIG_DEFINITION = sz_config.export()
    CONFIG_COMMENT = "Just an example"
    NEW_DEFAULT_CONFIG_ID = sz_configmanager.register_config(CONFIG_DEFINITION, CONFIG_COMMENT)

    # Replace default config id.

    sz_configmanager.replace_default_config_id(CURRENT_DEFAULT_CONFIG_ID, NEW_DEFAULT_CONFIG_ID)
except SzError as err:
    print(f"\nERROR: {err}\n")
