from senzing import SzError

from . import sz_configmanager

try:
    DATA_SOURCE_CODE = "TEST"
    sz_config = sz_configmanager.create_config_from_template()
    RESULT = sz_config.delete_data_source(DATA_SOURCE_CODE)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
