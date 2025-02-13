from senzing import SzEngineFlags, SzError

from . import sz_engine

try:
    flags = SzEngineFlags.SZ_WITH_INFO
    while True:
        redo_record = sz_engine.get_redo_record()
        if not redo_record:
            break
        RESULT = sz_engine.process_redo_record(redo_record, flags)
        print(RESULT)
except SzError as err:
    print(f"\nERROR: {err}\n")
