import time

from senzing import SzError

from . import sz_abstract_factory

try:
    CONFIG_COMMENT = "Just an example"
    data_source_code = f"REPLACE_DEFAULT_CONFIG_ID_{time.time()}"
    sz_config = sz_abstract_factory.create_config()
    sz_configmanager = sz_abstract_factory.create_configmanager()
    current_default_config_id = sz_configmanager.get_default_config_id()

    # Create a new config.

    current_config_definition = sz_configmanager.get_config(current_default_config_id)
    current_config_handle = sz_config.import_config(current_config_definition)
    sz_config.add_data_source(current_config_handle, data_source_code)
    new_config_definition = sz_config.export_config(current_config_handle)
    new_default_config_id = sz_configmanager.add_config(new_config_definition, CONFIG_COMMENT)

    # Replace default config id.

    sz_configmanager.replace_default_config_id(current_default_config_id, new_default_config_id)
except SzError as err:
    print(f"\nERROR: {err}\n")
