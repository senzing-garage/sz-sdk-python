#! /usr/bin/env python3

"""
TODO: szengine_test.py
"""

from typing import Any, Dict, List, Optional, Tuple, Union

import pytest

from senzing_abstract import SzEngineAbstract, SzEngineFlags

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_add_record(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().add_record()."""
    sz_engine.add_record("", "", "")


def test_close_export(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().close_export()."""
    sz_engine.close_export(0)


def test_count_redo_records(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().count_redo_records()."""
    sz_engine.count_redo_records()


def test_delete_record(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().delete_record()."""
    sz_engine.delete_record("", "")


# def test_destroy(sz_engine: SzEngineAbstract) -> None:
#     """Test SzEngine().destroy()."""
#     sz_engine.destroy()


def test_export_csv_entity_report(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().export_csv_entity_report()."""
    sz_engine.export_csv_entity_report("")


def test_export_json_entity_report(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().export_json_entity_report()."""
    sz_engine.export_json_entity_report()


def test_fetch_next(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().fetch_next()."""
    sz_engine.fetch_next(0)


def test_find_interesting_entities_by_entity_id(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().find_interesting_entities_by_entity_id()."""
    sz_engine.find_interesting_entities_by_entity_id(0)


def test_find_interesting_entities_by_record_id(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().find_interesting_entities_by_record_id()."""
    sz_engine.find_interesting_entities_by_record_id("", "")


def test_find_network_by_entity_id(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().find_network_by_entity_id()."""
    sz_engine.find_network_by_entity_id([], 0, 0, 0)


def test_find_network_by_record_id(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().find_network_by_record_id()."""
    sz_engine.find_network_by_record_id([], 0, 0, 0)


def test_find_path_by_entity_id(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().find_path_by_entity_id()."""
    sz_engine.find_path_by_entity_id(0, 0, 0)


def test_find_path_by_record_id(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().find_path_by_record_id()."""
    sz_engine.find_path_by_record_id("", "", "", "", 0)


def test_get_active_config_id(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().get_active_config_id()."""
    sz_engine.get_active_config_id()


def test_get_entity_by_entity_id(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().get_entity_by_entity_id()."""
    sz_engine.get_entity_by_entity_id(0)


def test_get_entity_by_record_id(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().get_entity_by_record_id()."""
    sz_engine.get_entity_by_record_id("", "")


def test_get_record(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().get_record()."""
    sz_engine.get_record("", "")


def test_get_redo_record(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().get_redo_record()."""
    sz_engine.get_redo_record()


def test_get_stats(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().stats()."""
    sz_engine.get_stats()


def test_get_virtual_entity_by_record_id(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().get_virtual_entity_by_record_id()."""
    sz_engine.get_virtual_entity_by_record_id([])


def test_how_entity_by_entity_id(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().how_entity_by_entity_id()."""
    sz_engine.how_entity_by_entity_id(0)


# def test_initialize(sz_engine: SzEngineAbstract) -> None:
#     """Test SzEngine().init()."""
#     sz_engine.initialize("", "")


def test_preprocess_record(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().preprocess_record()."""
    sz_engine.preprocess_record("")


def test_prime_engine(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().prime_engine()."""
    sz_engine.prime_engine()


def test_reevaluate_entity(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().reevaluate_entity()."""
    sz_engine.reevaluate_entity(0)


def test_reevaluate_record(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().reevaluate_record()."""
    sz_engine.reevaluate_record("", "")


def test_search_by_attributes(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().search_by_attributes()."""
    sz_engine.search_by_attributes("")


def test_why_entities(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().why_entities()."""
    sz_engine.why_entities(0, 0)


def test_why_record_in_entity(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().why_record_in_entity()."""
    sz_engine.why_record_in_entity("", "")


def test_why_records(sz_engine: SzEngineAbstract) -> None:
    """Test SzEngine().why_records()."""
    sz_engine.why_records("", "", "", "")


# -----------------------------------------------------------------------------
# SzEngine fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_engine", scope="module")
def szengine_fixture() -> SzEngineAbstract:
    """
    Object under test.
    """

    return SzEngineTest()


# -----------------------------------------------------------------------------
# SzEngineTest class
# -----------------------------------------------------------------------------


class SzEngineTest(SzEngineAbstract):
    """
    SzEngine module access library.
    """

    # -------------------------------------------------------------------------
    # SzEngine methods
    # -------------------------------------------------------------------------

    def add_record(
        self,
        data_source_code: str,
        record_id: str,
        record_definition: str,
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        return ""

    def close_export(self, export_handle: int, **kwargs: Any) -> None:
        """None"""

    def count_redo_records(self, **kwargs: Any) -> int:
        return 0

    def delete_record(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        return ""

    def destroy(self, **kwargs: Any) -> None:
        """None"""

    def export_csv_entity_report(
        self,
        csv_column_list: str,
        flags: int = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> int:
        return 0

    def export_json_entity_report(
        self, flags: int = SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS, **kwargs: Any
    ) -> int:
        return 0

    def fetch_next(self, export_handle: int, **kwargs: Any) -> str:
        return ""

    def find_interesting_entities_by_entity_id(
        self, entity_id: int, flags: int = 0, **kwargs: Any
    ) -> str:
        return ""

    def find_interesting_entities_by_record_id(
        self, data_source_code: str, record_id: str, flags: int = 0, **kwargs: Any
    ) -> str:
        return ""

    def find_network_by_entity_id(
        self,
        entity_ids: List[int],
        max_degrees: int,
        build_out_degree: int,
        build_out_max_entities: int,
        flags: int = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_network_by_record_id(
        self,
        record_keys: List[Tuple[str, str]],
        max_degrees: int,
        build_out_degree: int,
        build_out_max_entities: int,
        flags: int = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_path_by_entity_id(
        self,
        start_entity_id: int,
        end_entity_id: int,
        max_degrees: int,
        avoid_entity_ids: Optional[List[int]] = None,
        required_data_sources: Optional[List[str]] = None,
        flags: int = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_path_by_record_id(
        self,
        start_data_source_code: str,
        start_record_id: str,
        end_data_source_code: str,
        end_record_id: str,
        max_degrees: int,
        avoid_record_keys: Optional[List[Tuple[str, str]]] = None,
        required_data_sources: Optional[List[str]] = None,
        flags: int = SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def get_active_config_id(self, **kwargs: Any) -> int:
        return 0

    def get_entity_by_entity_id(
        self,
        entity_id: int,
        flags: int = SzEngineFlags.SZ_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def get_entity_by_record_id(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = SzEngineFlags.SZ_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def get_record(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = SzEngineFlags.SZ_RECORD_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def get_redo_record(self, **kwargs: Any) -> str:
        return ""

    def get_stats(self, **kwargs: Any) -> str:
        return ""

    def get_virtual_entity_by_record_id(
        self,
        record_keys: List[Tuple[str, str]],
        flags: int = SzEngineFlags.SZ_VIRTUAL_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def how_entity_by_entity_id(
        self,
        entity_id: int,
        flags: int = SzEngineFlags.SZ_HOW_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def initialize(
        self,
        instance_name: str,
        settings: Union[str, Dict[Any, Any]],
        config_id: Optional[int] = 0,
        verbose_logging: Optional[int] = 0,
        **kwargs: Any,
    ) -> None:
        """None"""

    def preprocess_record(
        self,
        record_definition: str,
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        return ""

    def prime_engine(self, **kwargs: Any) -> None:
        """None"""

    def process_redo_record(self, redo_record: str, flags: int, **kwargs: Any) -> str:
        return ""

    def reevaluate_entity(self, entity_id: int, flags: int = 0, **kwargs: Any) -> str:
        return ""

    def reevaluate_record(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        return ""

    def reinitialize(self, config_id: int, **kwargs: Any) -> None:
        """None"""

    def search_by_attributes(
        self,
        attributes: str,
        flags: int = SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS,
        search_profile: str = "",
        **kwargs: Any,
    ) -> str:
        return ""

    def why_entities(
        self,
        entity_id_1: int,
        entity_id_2: int,
        flags: int = SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def why_record_in_entity(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = SzEngineFlags.SZ_WHY_RECORDS_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def why_records(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        flags: int = SzEngineFlags.SZ_WHY_RECORDS_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""
