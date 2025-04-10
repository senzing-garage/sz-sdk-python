from senzing import SzError

from . import sz_engine

try:
    RESULT = sz_engine.count_redo_records()
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
