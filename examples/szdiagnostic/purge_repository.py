#! /usr/bin/env python3
from senzing import SzError

from .setup_senzing import get_sz_abstract_factory

try:
    sz_abstract_factory = get_sz_abstract_factory()
    sz_diagnostic = sz_abstract_factory.create_diagnostic()
    # WARNING
    # WARNING - This will remove all loaded and entity resolved data from the Senzing repository, use with caution!
    # WARNING - Uncomment the purge_repository() call below to complete a purge
    # WARNING

    # sz_diagnostic.purge_repository()
except SzError as err:
    print(f"\nERROR: {err}\n")
