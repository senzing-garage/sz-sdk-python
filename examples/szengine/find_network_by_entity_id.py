#! /usr/bin/env python3

from senzing_xxxx import (
    SzAbstractFactory,
    SzAbstractFactoryParameters,
    SzEngineFlags,
    SzError,
)

BUILD_OUT_DEGREES = 1
ENTITY_LIST = [1, 4]
FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    # Differs based on which senzing_xxxx package is used.
}
FLAGS = SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS
MAX_DEGREES = 2
MAX_ENTITIES = 10

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.find_network_by_entity_id(ENTITY_LIST, MAX_DEGREES, BUILD_OUT_DEGREES, MAX_ENTITIES, FLAGS)
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
