#! /usr/bin/env python3

"""
TODO: szengine_test.py
"""


import pytest

from senzing import SzEngine
from senzing_mock import SzEngineMock

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_add_record(sz_engine: SzEngine) -> None:
    """Test SzEngine().add_record()."""
    sz_engine.add_record("", "", "")


def test_close_export(sz_engine: SzEngine) -> None:
    """Test SzEngine().close_export()."""
    sz_engine.close_export(0)


def test_count_redo_records(sz_engine: SzEngine) -> None:
    """Test SzEngine().count_redo_records()."""
    sz_engine.count_redo_records()


def test_delete_record(sz_engine: SzEngine) -> None:
    """Test SzEngine().delete_record()."""
    sz_engine.delete_record("", "")


# def test_destroy(sz_engine: SzEngine) -> None:
#     """Test SzEngine().destroy()."""
#     sz_engine.destroy()


def test_export_csv_entity_report(sz_engine: SzEngine) -> None:
    """Test SzEngine().export_csv_entity_report()."""
    sz_engine.export_csv_entity_report("")


def test_export_json_entity_report(sz_engine: SzEngine) -> None:
    """Test SzEngine().export_json_entity_report()."""
    sz_engine.export_json_entity_report()


def test_fetch_next(sz_engine: SzEngine) -> None:
    """Test SzEngine().fetch_next()."""
    sz_engine.fetch_next(0)


def test_find_interesting_entities_by_entity_id(sz_engine: SzEngine) -> None:
    """Test SzEngine().find_interesting_entities_by_entity_id()."""
    sz_engine.find_interesting_entities_by_entity_id(0)


def test_find_interesting_entities_by_record_id(sz_engine: SzEngine) -> None:
    """Test SzEngine().find_interesting_entities_by_record_id()."""
    sz_engine.find_interesting_entities_by_record_id("", "")


def test_find_network_by_entity_id(sz_engine: SzEngine) -> None:
    """Test SzEngine().find_network_by_entity_id()."""
    sz_engine.find_network_by_entity_id([], 0, 0, 0)


def test_find_network_by_record_id(sz_engine: SzEngine) -> None:
    """Test SzEngine().find_network_by_record_id()."""
    sz_engine.find_network_by_record_id([], 0, 0, 0)


def test_find_path_by_entity_id(sz_engine: SzEngine) -> None:
    """Test SzEngine().find_path_by_entity_id()."""
    sz_engine.find_path_by_entity_id(0, 0, 0)


def test_find_path_by_record_id(sz_engine: SzEngine) -> None:
    """Test SzEngine().find_path_by_record_id()."""
    sz_engine.find_path_by_record_id("", "", "", "", 0)


def test_get_active_config_id(sz_engine: SzEngine) -> None:
    """Test SzEngine().get_active_config_id()."""
    sz_engine.get_active_config_id()


def test_get_entity_by_entity_id(sz_engine: SzEngine) -> None:
    """Test SzEngine().get_entity_by_entity_id()."""
    sz_engine.get_entity_by_entity_id(0)


def test_get_entity_by_record_id(sz_engine: SzEngine) -> None:
    """Test SzEngine().get_entity_by_record_id()."""
    sz_engine.get_entity_by_record_id("", "")


def test_get_record(sz_engine: SzEngine) -> None:
    """Test SzEngine().get_record()."""
    sz_engine.get_record("", "")


def test_get_redo_record(sz_engine: SzEngine) -> None:
    """Test SzEngine().get_redo_record()."""
    sz_engine.get_redo_record()


def test_get_stats(sz_engine: SzEngine) -> None:
    """Test SzEngine().stats()."""
    sz_engine.get_stats()


def test_get_virtual_entity_by_record_id(sz_engine: SzEngine) -> None:
    """Test SzEngine().get_virtual_entity_by_record_id()."""
    sz_engine.get_virtual_entity_by_record_id([])


def test_help_1(sz_engine: SzEngine) -> None:
    """Test SzEngine().help()."""
    sz_engine.help()


def test_help_2(sz_engine: SzEngine) -> None:
    """Test SzEngine().help(...)."""
    sz_engine.help("get_stats")


def test_how_entity_by_entity_id(sz_engine: SzEngine) -> None:
    """Test SzEngine().how_entity_by_entity_id()."""
    sz_engine.how_entity_by_entity_id(0)


# def test_initialize(sz_engine: SzEngine) -> None:
#     """Test SzEngine().init()."""
#     sz_engine.initialize("", "")


def test_preprocess_record(sz_engine: SzEngine) -> None:
    """Test SzEngine().preprocess_record()."""
    sz_engine.preprocess_record("")


def test_prime_engine(sz_engine: SzEngine) -> None:
    """Test SzEngine().prime_engine()."""
    sz_engine.prime_engine()


def test_process_redo_record(sz_engine: SzEngine) -> None:
    """Test SzEngine().process_redo_record()."""
    sz_engine.process_redo_record("")


def test_reevaluate_entity(sz_engine: SzEngine) -> None:
    """Test SzEngine().reevaluate_entity()."""
    sz_engine.reevaluate_entity(0)


def test_reevaluate_record(sz_engine: SzEngine) -> None:
    """Test SzEngine().reevaluate_record()."""
    sz_engine.reevaluate_record("", "")


def test_search_by_attributes(sz_engine: SzEngine) -> None:
    """Test SzEngine().search_by_attributes()."""
    sz_engine.search_by_attributes("")


def test_why_entities(sz_engine: SzEngine) -> None:
    """Test SzEngine().why_entities()."""
    sz_engine.why_entities(0, 0)


def test_why_record_in_entity(sz_engine: SzEngine) -> None:
    """Test SzEngine().why_record_in_entity()."""
    sz_engine.why_record_in_entity("", "")


def test_why_records(sz_engine: SzEngine) -> None:
    """Test SzEngine().why_records()."""
    sz_engine.why_records("", "", "", "")


def test_why_search(sz_engine: SzEngine) -> None:
    """Test SzEngine().why_search()."""
    sz_engine.why_search("", 0)


# -----------------------------------------------------------------------------
# SzEngine fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_engine", scope="module")
def szengine_fixture() -> SzEngine:
    """
    Object under test.
    """

    return SzEngineMock()
