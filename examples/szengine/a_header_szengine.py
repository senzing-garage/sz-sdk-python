"""
Simply a header used in development.
"""

from typing import List, Tuple

from senzing import SZ_WITHOUT_INFO, SzAbstractFactory
from senzing_truthset import (
    TRUTHSET_CUSTOMER_RECORDS,
    TRUTHSET_REFERENCE_RECORDS,
    TRUTHSET_WATCHLIST_RECORDS,
)

from . import sz_abstract_factory

DATA_SOURCES = {
    "CUSTOMERS": TRUTHSET_CUSTOMER_RECORDS,
    "REFERENCE": TRUTHSET_REFERENCE_RECORDS,
    "WATCHLIST": TRUTHSET_WATCHLIST_RECORDS,
}


TEST_RECORDS: List[Tuple[str, str]] = [
    ("CUSTOMERS", "1001"),
    ("CUSTOMERS", "1002"),
    ("CUSTOMERS", "1003"),
    ("CUSTOMERS", "1009"),
]

# -----------------------------------------------------------------------------
# Internal functions
# -----------------------------------------------------------------------------


def add_data_sources(sz_abstract_factory_local: SzAbstractFactory, data_sources: List[str]) -> None:
    """Add all of the records in the list."""

    sz_configmanager = sz_abstract_factory_local.create_configmanager()
    sz_config = sz_abstract_factory_local.create_config()
    default_config_id = sz_configmanager.get_default_config_id()
    old_config_definition = sz_configmanager.get_config(default_config_id)
    config_handle = sz_config.import_config(old_config_definition)
    for data_source in data_sources:
        sz_config.add_data_source(config_handle, data_source)
    new_config_definition = sz_config.export_config(config_handle)
    sz_config.close_config(config_handle)
    new_config_id = sz_configmanager.add_config(new_config_definition, "Test")
    sz_configmanager.replace_default_config_id(default_config_id, new_config_id)
    sz_abstract_factory_local.reinitialize(new_config_id)


def add_records(sz_abstract_factory_local: SzAbstractFactory, record_id_list: List[Tuple[str, str]]) -> None:
    """Add all of the records in the list."""
    sz_engine_local = sz_abstract_factory_local.create_engine()
    flags = SZ_WITHOUT_INFO
    for record_identification in record_id_list:
        datasource = record_identification[0]
        record_id = record_identification[1]
        record = DATA_SOURCES.get(datasource, {}).get(record_id, {})
        sz_engine_local.add_record(
            record.get("DataSource", ""),
            record.get("Id", ""),
            record.get("Json", ""),
            flags,
        )


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

print("\n---- szengine --------------------------------------------------------\n")

x = DATA_SOURCES.keys()
add_data_sources(sz_abstract_factory, list(DATA_SOURCES.keys()))
add_records(sz_abstract_factory, TEST_RECORDS)
