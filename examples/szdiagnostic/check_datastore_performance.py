from senzing import SzError

from . import sz_diagnostic

try:
    SECONDS_TO_RUN = 3
    result = sz_diagnostic.check_datastore_performance(SECONDS_TO_RUN)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
