from senzing import SzError

from . import get_sz_abstract_factory

sz_abstract_factory = get_sz_abstract_factory()
try:
    sz_config = sz_abstract_factory.create_config()
    sz_configmanager = sz_abstract_factory.create_configmanager()
    config_id = sz_configmanager.get_default_config_id()
    config_definition = sz_configmanager.get_config(config_id)
    config_handle = sz_config.import_config(config_definition)
except SzError as err:
    print(f"\nERROR: {err}\n")
