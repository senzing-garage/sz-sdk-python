#! /usr/bin/env python3
from senzing import SzError

from . import get_sz_diagnostic

sz_diagnostic = get_sz_diagnostic()
try:
    RESULT = sz_diagnostic.get_datastore_info()
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
