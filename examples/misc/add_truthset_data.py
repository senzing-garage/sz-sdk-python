from senzing import SZ_WITHOUT_INFO, SzError
from senzing_truthset import (
    TRUTHSET_CUSTOMER_RECORDS,
    TRUTHSET_REFERENCE_RECORDS,
    TRUTHSET_WATCHLIST_RECORDS,
)

from . import sz_abstract_factory

record_sets = [
    TRUTHSET_CUSTOMER_RECORDS,
    TRUTHSET_REFERENCE_RECORDS,
    TRUTHSET_WATCHLIST_RECORDS,
]

try:
    sz_engine = sz_abstract_factory.create_engine()
    for record_set in record_sets:
        for record in record_set.values():
            sz_engine.add_record(
                record.get("DataSource"),
                record.get("Id"),
                record.get("Json"),
                SZ_WITHOUT_INFO,
            )
except SzError as err:
    print(f"\nERROR: {err}\n")
