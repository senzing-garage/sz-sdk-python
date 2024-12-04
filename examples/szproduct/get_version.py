#! /usr/bin/env python3

from senzing_xxxx import SzAbstractFactory, SzAbstractFactoryParameters, SzError

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    # Differs based on which senzing_xxxx package is used.
}

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_product = sz_abstract_factory.create_product()
    RESULT = sz_product.get_version()
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
