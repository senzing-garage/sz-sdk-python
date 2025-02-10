#! /usr/bin/env python3
from senzing import SzError

from setup_senzing import get_sz_abstract_factory

try:
    sz_abstract_factory = get_sz_abstract_factory()
    sz_diagnostic = sz_abstract_factory.create_diagnostic()
    RESULT = sz_diagnostic.get_feature(1)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
