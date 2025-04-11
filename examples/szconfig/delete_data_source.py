from senzing import SzError

from . import sz_configmanager

try:
    DATA_SOURCE_CODE = "TEST"
    sz_config = sz_configmanager.create_config_from_template()
    _ = sz_config.delete_data_source(DATA_SOURCE_CODE)
except SzError as err:
    print(f"\nERROR: {err}\n")
