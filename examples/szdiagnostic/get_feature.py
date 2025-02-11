#! /usr/bin/env python3
from senzing import SzError

from . import get_sz_diagnostic

try:
    sz_diagnostic = get_sz_diagnostic()
    RESULT = sz_diagnostic.get_feature(1)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
