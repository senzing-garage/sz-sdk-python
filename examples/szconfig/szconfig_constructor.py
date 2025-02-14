from senzing import SzError

from . import sz_abstract_factory

try:
    sz_config = sz_abstract_factory.create_config()
except SzError as err:
    print(f"\nERROR: {err}\n")
