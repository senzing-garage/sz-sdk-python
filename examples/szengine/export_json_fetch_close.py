from senzing import SzEngineFlags, SzError

from . import sz_engine

flags = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS

try:
    export_handle = sz_engine.export_json_entity_report(flags)
    while True:
        fragment = sz_engine.fetch_next(export_handle)
        if not fragment:
            break
        print(fragment, end="")
    sz_engine.close_export(export_handle)
except SzError as err:
    print(f"\nERROR: {err}\n")
