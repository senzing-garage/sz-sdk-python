from senzing import SzError

from . import sz_configmanager

try:
    config_comment = "Just an empty example"
    sz_config = sz_configmanager.create_config_from_template()
    config_definition = sz_config.export()
    config_id = sz_configmanager.register_config(config_definition, config_comment)
except SzError as err:
    print(f"\nERROR: {err}\n")
