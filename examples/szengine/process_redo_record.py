#! /usr/bin/env python3
from senzing import SzEngineFlags, SzError

from . import get_sz_abstract_factory

FLAGS = SzEngineFlags.SZ_WITH_INFO
try:
    sz_abstract_factory = get_sz_abstract_factory()
    sz_engine = sz_abstract_factory.create_engine()
    while True:
        redo_record = sz_engine.get_redo_record()
        if not redo_record:
            break
        RESULT = sz_engine.process_redo_record(redo_record, FLAGS)
        print(RESULT)
except SzError as err:
    print(f"\nERROR: {err}\n")
