#! /usr/bin/env python3
from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
CSV_COLUMN_LIST = (
    "RESOLVED_ENTITY_ID,RELATED_ENTITY_ID,RESOLVED_ENTITY_NAME,MATCH_LEVEL,MATCH_KEY,DATA_SOURCE,RECORD_ID"
)
FLAGS = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS
try:
    export_handle = sz_engine.export_csv_entity_report(CSV_COLUMN_LIST, FLAGS)
    while True:
        fragment = sz_engine.fetch_next(export_handle)
        if not fragment:
            break
        print(fragment, end="")
    sz_engine.close_export(export_handle)
except SzError as err:
    print(f"\nERROR: {err}\n")
