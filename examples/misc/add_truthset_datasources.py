from senzing import SzError
from senzing_truthset import TRUTHSET_DATASOURCES

from . import get_sz_abstract_factory

try:
    sz_abstract_factory = get_sz_abstract_factory()
    sz_config = sz_abstract_factory.create_config()
    sz_configmanager = sz_abstract_factory.create_configmanager()
    sz_diagnostic = sz_abstract_factory.create_diagnostic()
    sz_engine = sz_abstract_factory.create_engine()

    current_default_config_id = sz_configmanager.get_default_config_id()
    old_config_definition = sz_configmanager.get_config(current_default_config_id)
    config_handle = sz_config.import_config(old_config_definition)
    for data_source_code in TRUTHSET_DATASOURCES:
        sz_config.add_data_source(config_handle, data_source_code)
    new_config_definition = sz_config.export_config(config_handle)
    new_default_config_id = sz_configmanager.add_config(new_config_definition, "Add TruthSet datasources")
    sz_configmanager.replace_default_config_id(current_default_config_id, new_default_config_id)
    sz_abstract_factory.reinitialize(new_default_config_id)
except SzError as err:
    print(f"\nERROR: {err}\n")
