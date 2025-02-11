#! /usr/bin/env python3
from senzing import SzEngineFlags, SzError

from . import get_sz_abstract_factory

FLAGS = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS
try:
    sz_abstract_factory = get_sz_abstract_factory()
    sz_engine = sz_abstract_factory.create_engine()
    export_handle = sz_engine.export_json_entity_report(FLAGS)
    while True:
        fragment = sz_engine.fetch_next(export_handle)
        if not fragment:
            break
        print(fragment, end="")
    sz_engine.close_export(export_handle)
except SzError as err:
    print(f"\nERROR: {err}\n")
