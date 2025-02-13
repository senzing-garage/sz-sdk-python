from senzing import SzError

from . import sz_abstract_factory

try:
    sz_configmanager = sz_abstract_factory.create_configmanager()
except SzError as err:
    print(f"\nERROR: {err}\n")
