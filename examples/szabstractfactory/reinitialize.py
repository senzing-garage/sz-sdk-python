#! /usr/bin/env python3

from senzing_xxxx import SzAbstractFactory, SzAbstractFactoryParameters, SzError

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    # Differs based on implementation
}

try:
    # Using get_active_config_id for demonstrations purposes.
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_engine()
    config_id = sz_engine.get_active_config_id()
    sz_abstract_factory.reinitialize(config_id)
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
