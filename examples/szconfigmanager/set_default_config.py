import time

from senzing import SzError

from . import sz_configmanager

try:

    # Create a new config.

    sz_config = sz_configmanager.create_config_from_template()
    data_source_code = f"REPLACE_DEFAULT_CONFIG_ID_{time.time()}"
    sz_config.add_data_source(data_source_code)

    # Persist the new default config.

    config_definition = sz_config.export()
    CONFIG_COMMENT = "Just an example"
    config_id = sz_configmanager.set_default_config(config_definition, CONFIG_COMMENT)

except SzError as err:
    print(f"\nERROR: {err}\n")
