import json

from senzing import SzEngineFlags, SzError

from . import get_sz_engine

sz_engine = get_sz_engine()
FLAGS = SzEngineFlags.SZ_RECORD_DEFAULT_FLAGS
RECORD_DEFINITION = json.dumps(
    {
        "RECORD_TYPE": "PERSON",
        "PRIMARY_NAME_LAST": "Smith",
        "PRIMARY_NAME_FIRST": "Robert",
        "DATE_OF_BIRTH": "12/11/1978",
        "ADDR_TYPE": "MAILING",
        "ADDR_LINE1": "123 Main Street, Las Vegas NV 89132",
        "PHONE_TYPE": "HOME",
        "PHONE_NUMBER": "702-919-1300",
        "EMAIL_ADDRESS": "bsmith@work.com",
        "DATE": "1/2/18",
        "STATUS": "Active",
        "AMOUNT": "100",
    }
)
try:
    RESULT = sz_engine.preprocess_record(RECORD_DEFINITION, FLAGS)
    print(f"\n{RESULT}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
