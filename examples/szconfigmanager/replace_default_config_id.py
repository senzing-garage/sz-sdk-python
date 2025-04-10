import time

from senzing import SzError

from . import sz_configmanager

try:
    sz_config = sz_configmanager.create_config_from_template()
    current_default_config_id = sz_configmanager.get_default_config_id()

    # Create a new config.

    sz_config = sz_configmanager.create_config_from_config_id(current_default_config_id)
    data_source_code = f"REPLACE_DEFAULT_CONFIG_ID_{time.time()}"
    sz_config.add_data_source(data_source_code)

    # Persist the new config.

    config_definition = sz_config.export()
    CONFIG_COMMENT = "Just an example"
    new_default_config_id = sz_configmanager.register_config(config_definition, CONFIG_COMMENT)

    # Replace default config id.

    sz_configmanager.replace_default_config_id(current_default_config_id, new_default_config_id)
except SzError as err:
    print(f"\nERROR: {err}\n")
