from senzing import SzEngineFlags, SzError

from . import sz_engine

try:
    CSV_COLUMN_LIST = (
        "RESOLVED_ENTITY_ID,RELATED_ENTITY_ID,RESOLVED_ENTITY_NAME,MATCH_LEVEL,MATCH_KEY,DATA_SOURCE,RECORD_ID"
    )
    flags = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS
    EXPORT_HANDLE = sz_engine.export_csv_entity_report(CSV_COLUMN_LIST, flags)
    while True:
        FRAGMENT = sz_engine.fetch_next(EXPORT_HANDLE)
        if not FRAGMENT:
            break
        print(FRAGMENT, end="")
    sz_engine.close_export(EXPORT_HANDLE)
except SzError as err:
    print(f"\nERROR: {err}\n")
