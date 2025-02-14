import json

from senzing import SzEngineFlags, SzError

from . import sz_engine

try:
    DATA_SOURCE_CODE = "TEST"
    flags = SzEngineFlags.SZ_WITH_INFO
    record_definition = json.dumps(
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
    RECORD_ID = "1"
    result = sz_engine.add_record(DATA_SOURCE_CODE, RECORD_ID, record_definition, flags)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
