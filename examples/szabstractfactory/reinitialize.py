#! /usr/bin/env python3
from senzing import SzError

from .setup_senzing import get_sz_abstract_factory

try:
    # Using get_active_config_id for demonstrations purposes.
    sz_abstract_factory = get_sz_abstract_factory()
    sz_engine = sz_abstract_factory.create_engine()
    config_id = sz_engine.get_active_config_id()
    sz_abstract_factory.reinitialize(config_id)
except SzError as err:
    print(f"\nERROR: {err}\n")
