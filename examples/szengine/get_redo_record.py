from senzing import SzError

from . import sz_engine

try:
    RESULT = sz_engine.get_redo_record()
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
