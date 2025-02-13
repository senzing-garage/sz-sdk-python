import time

from senzing import SzError

from . import get_sz_abstract_factory

sz_abstract_factory = get_sz_abstract_factory()
try:
    CONFIG_COMMENT = "Just an example"
    data_source_code = f"REPLACE_DEFAULT_CONFIG_ID_{time.time()}"
    sz_config = sz_abstract_factory.create_config()
    sz_configmanager = sz_abstract_factory.create_configmanager()
    old_config_id = sz_configmanager.get_default_config_id()

    # Create a new config.

    old_config_definition = sz_configmanager.get_config(old_config_id)
    old_config_handle = sz_config.import_config(old_config_definition)
    sz_config.add_data_source(old_config_handle, data_source_code)
    new_config_definition = sz_config.export_config(old_config_handle)
    config_id = sz_configmanager.add_config(new_config_definition, CONFIG_COMMENT)

    # Set default config id.

    sz_configmanager.set_default_config_id(config_id)
except SzError as err:
    print(f"\nERROR: {err}\n")
