from senzing import SzEngineFlags, SzError

from . import sz_engine

flags = SzEngineFlags.SZ_WITH_INFO

try:
    while True:
        redo_record = sz_engine.get_redo_record()
        if not redo_record:
            break
        result = sz_engine.process_redo_record(redo_record, flags)
        print(result)
except SzError as err:
    print(f"\nERROR: {err}\n")
