from senzing import SzError

from . import sz_abstract_factory

try:
    sz_product = sz_abstract_factory.create_product()
except SzError as err:
    print(f"\nERROR: {err}\n")
