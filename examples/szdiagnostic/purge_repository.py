from senzing import SzError

from . import sz_diagnostic

try:
    _ = sz_diagnostic
    # WARNING
    # WARNING - This will remove all loaded and entity resolved data from the Senzing repository, use with caution!
    # WARNING - Uncomment the purge_repository() call below to complete a purge
    # WARNING

    # sz_diagnostic.purge_repository()
except SzError as err:
    print(f"\nERROR: {err}\n")
