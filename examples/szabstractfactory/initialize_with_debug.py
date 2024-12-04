#! /usr/bin/env python3

from senzing_xxxx import SzAbstractFactory, SzAbstractFactoryParameters, SzError

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    # Differs based on implementation
}

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
