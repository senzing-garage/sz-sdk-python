#! /usr/bin/env python3

from senzing_xxxx import SzAbstractFactory, SzAbstractFactoryParameters, SzError

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    # Differs based on implementation
}

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_configmanager = sz_abstract_factory.create_configmanager()
    CONFIG_ID = sz_configmanager.get_default_config_id()
    print(f"\nFile {__file__}:\n{CONFIG_ID}\n")
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
