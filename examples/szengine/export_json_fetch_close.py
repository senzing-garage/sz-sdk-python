from senzing import SzEngineFlags, SzError

from . import sz_engine

try:
    flags = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS
    EXPORT_HANDLE = sz_engine.export_json_entity_report(flags)
    while True:
        FRAGMENT = sz_engine.fetch_next(EXPORT_HANDLE)
        if not FRAGMENT:
            break
        print(FRAGMENT, end="")
    sz_engine.close_export(EXPORT_HANDLE)
except SzError as err:
    print(f"\nERROR: {err}\n")
