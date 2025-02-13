from senzing import SzError

from . import sz_diagnostic

try:
    result = sz_diagnostic.get_feature(1)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
