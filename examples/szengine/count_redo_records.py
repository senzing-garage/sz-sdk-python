from senzing import SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
try:
    result = sz_engine.count_redo_records()
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
