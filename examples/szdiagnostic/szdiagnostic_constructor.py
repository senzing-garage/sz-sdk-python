from senzing import SzError

from . import sz_abstract_factory

try:
    sz_diagnostic = sz_abstract_factory.create_diagnostic()
except SzError as err:
    print(f"\nERROR: {err}\n")
