from senzing import SzError

from . import get_sz_abstract_factory

sz_abstract_factory = get_sz_abstract_factory()
try:
    sz_config = sz_abstract_factory.create_config()
except SzError as err:
    print(f"\nERROR: {err}\n")
