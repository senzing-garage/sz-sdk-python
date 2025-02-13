from senzing import SzError

from . import sz_abstract_factory

try:
    sz_engine = sz_abstract_factory.create_engine()
except SzError as err:
    print(f"\nERROR: {err}\n")
