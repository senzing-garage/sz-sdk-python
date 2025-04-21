from senzing import SzError

from . import sz_diagnostic

seconds_to_run = 3

try:
    result = sz_diagnostic.check_datastore_performance(seconds_to_run)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
