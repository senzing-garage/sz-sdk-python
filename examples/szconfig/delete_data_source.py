from senzing import SzError

from . import sz_configmanager

data_source_code = "TEST"

try:
    sz_config = sz_configmanager.create_config_from_template()
    _ = sz_config.delete_data_source(data_source_code)
except SzError as err:
    print(f"\nERROR: {err}\n")
