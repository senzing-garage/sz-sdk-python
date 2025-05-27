import json

from senzing import SzEngineFlags, SzError

from . import sz_engine

data_source_code = "TEST"
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
record_id = "1"

try:
    result = sz_engine.add_record(data_source_code, record_id, record_definition, flags)
    print(f"\n{result}\n")
except SzError as err:
    print(f"\nERROR: {err}\n")
