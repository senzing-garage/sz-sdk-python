from senzing import SzError

from . import sz_engine

try:
    result = sz_engine.get_stats()
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
