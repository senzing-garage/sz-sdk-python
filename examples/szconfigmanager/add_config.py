from senzing import SzError

from . import sz_abstract_factory

try:
    CONFIG_COMMENT = "Just an empty example"
    sz_config = sz_abstract_factory.create_config()
    sz_configmanager = sz_abstract_factory.create_configmanager()
    config_handle = sz_config.create_config()
    config_definition = sz_config.export_config(config_handle)
    config_id = sz_configmanager.add_config(config_definition, CONFIG_COMMENT)
except SzError as err:
    print(f"\nERROR: {err}\n")
