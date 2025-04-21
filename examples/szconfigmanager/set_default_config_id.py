import time

from senzing import SzError

from . import sz_configmanager

config_comment = "Just an example"
data_source_code = f"REPLACE_DEFAULT_CONFIG_ID_{time.time()}"

try:

    # Create a new config.

    sz_config = sz_configmanager.create_config_from_template()
    sz_config.add_data_source(data_source_code)

    # Persist the new config.

    config_definition = sz_config.export()
    new_default_config_id = sz_configmanager.register_config(config_definition, config_comment)

    # Set default config id.

    sz_configmanager.set_default_config_id(new_default_config_id)
except SzError as err:
    print(f"\nERROR: {err}\n")
