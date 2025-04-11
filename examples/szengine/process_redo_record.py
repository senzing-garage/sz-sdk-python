from senzing import SzEngineFlags, SzError

from . import sz_engine

try:
    flags = SzEngineFlags.SZ_WITH_INFO
    while True:
        REDO_RECORD = sz_engine.get_redo_record()
        if not REDO_RECORD:
            break
        RESULT = sz_engine.process_redo_record(REDO_RECORD, flags)
        print(RESULT)
except SzError as err:
    print(f"\nERROR: {err}\n")
