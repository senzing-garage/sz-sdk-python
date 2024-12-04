#! /usr/bin/env python3

from senzing_xxxx import (
    SzAbstractFactory,
    SzAbstractFactoryParameters,
    SzEngineFlags,
    SzError,
)

ENTITY_ID = 1
FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    # Differs based on which senzing_xxxx package is used.
}
FLAGS = SzEngineFlags.SZ_HOW_ENTITY_DEFAULT_FLAGS

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_engine()
    RESULT = sz_engine.how_entity_by_entity_id(ENTITY_ID, FLAGS)
    print(f"\nFile {__file__}:\n{RESULT}\n")
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
