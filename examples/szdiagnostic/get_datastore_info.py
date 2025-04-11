from senzing import SzError

from . import sz_diagnostic

try:
    RESULT = sz_diagnostic.get_datastore_info()
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
