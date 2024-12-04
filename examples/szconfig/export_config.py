#! /usr/bin/env python3

from senzing_xxxx import SzAbstractFactory, SzAbstractFactoryParameters, SzError

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    # Differs based on which senzing_xxxx package is used.
}

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_config = sz_abstract_factory.create_config()
    config_handle = sz_config.create_config()  # Create first in-memory.
    CONFIG_DEFINITION = sz_config.export_config(config_handle)  # Save in-memory to string.
    sz_config.close_config(config_handle)
    print(f"\nFile {__file__}:\n{CONFIG_DEFINITION}\n")
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
