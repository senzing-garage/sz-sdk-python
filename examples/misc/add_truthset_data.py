#! /usr/bin/env python3

from senzing_xxxx import (
    SZ_WITHOUT_INFO,
    SzAbstractFactory,
    SzAbstractFactoryParameters,
    SzError,
)

from senzing_truthset import (
    TRUTHSET_CUSTOMER_RECORDS,
    TRUTHSET_REFERENCE_RECORDS,
    TRUTHSET_WATCHLIST_RECORDS,
)

FACTORY_PARAMETERS: SzAbstractFactoryParameters = {
    # Differs based on which senzing_xxxx package is used.
}

try:
    sz_abstract_factory = SzAbstractFactory(**FACTORY_PARAMETERS)
    sz_engine = sz_abstract_factory.create_engine()
    record_sets = [
        TRUTHSET_CUSTOMER_RECORDS,
        TRUTHSET_REFERENCE_RECORDS,
        TRUTHSET_WATCHLIST_RECORDS,
    ]
    for record_set in record_sets:
        for record in record_set.values():
            sz_engine.add_record(
                record.get("DataSource"),
                record.get("Id"),
                record.get("Json"),
                SZ_WITHOUT_INFO,
            )
except SzError as err:
    print(f"\nFile {__file__}:\nError:\n{err}\n")
