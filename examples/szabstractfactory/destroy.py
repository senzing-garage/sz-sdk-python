from senzing import SzError

from . import sz_abstract_factory

try:
    sz_abstract_factory.destroy()
except SzError as err:
    print(f"\nERROR: {err}\n")
