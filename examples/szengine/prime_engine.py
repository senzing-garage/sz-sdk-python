from senzing import SzError

from . import sz_engine

try:
    sz_engine.prime_engine()
except SzError as err:
    print(f"\nERROR: {err}\n")
