from senzing import SzError

from . import get_sz_diagnostic

sz_diagnostic = get_sz_diagnostic()
try:
    SECONDS_TO_RUN = 3
    RESULT = sz_diagnostic.check_datastore_performance(SECONDS_TO_RUN)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
