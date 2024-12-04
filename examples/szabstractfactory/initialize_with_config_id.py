#! /usr/bin/env python3

from senzing_xxxx import SzAbstractFactory, SzAbstractFactoryParameters, SzError

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    # Differs based on which senzing_xxxx package is used.
}

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_configmanager = sz_abstract_factory.create_configmanager()
    config_id = sz_configmanager.get_default_config_id()
    sz_abstract_factory.reinitialize(config_id)
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
