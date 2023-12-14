#! /usr/bin/env python3

"""
TODO: g2engine_test.py
"""

# pylint: disable=E1101

from typing import Any, Dict, Iterable, Tuple, Union

import pytest

from senzing_abstract import g2engine_abstract
from senzing_abstract.g2engineflags import G2EngineFlags

# -----------------------------------------------------------------------------
# G2Engine fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="g2_engine", scope="module")  # type: ignore[misc]
def g2engine_fixture() -> g2engine_abstract.G2EngineAbstract:
    """
    Object under test.
    """

    return G2EngineTest()


# -----------------------------------------------------------------------------
# G2EngineTest class
# -----------------------------------------------------------------------------


class G2EngineTest(g2engine_abstract.G2EngineAbstract):
    """
    G2 engine module access library.
    """

    # -------------------------------------------------------------------------
    # G2Engine methods
    # -------------------------------------------------------------------------

    def add_record(
        self,
        data_source_code: str,
        record_id: str,
        json_data: Union[str, Dict[Any, Any]],
        # TODO: load_id is no longer used, being removed from V4 C api?
        load_id: str = "",
        flags: int = 0,  # pylint: disable=W0613
        **kwargs: Any,
    ) -> None:
        """None"""

    def add_record_with_info(
        self,
        data_source_code: str,
        record_id: str,
        json_data: Union[str, Dict[Any, Any]],
        # TODO: load_id is no longer used, being removed from V4 C api?
        load_id: str = "",
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        return ""

    def close_export(self, response_handle: int, **kwargs: Any) -> None:
        """None"""

    def count_redo_records(self, **kwargs: Any) -> int:
        return 0

    def delete_record(
        self,
        data_source_code: str,
        record_id: str,
        # TODO: load_id is no longer used, being removed from V4 C api?
        load_id: str = "",
        **kwargs: Any,
    ) -> None:
        """None"""

    def delete_record_with_info(
        self,
        data_source_code: str,
        record_id: str,
        # TODO: load_id is no longer used, being removed from V4 C api?
        load_id: str = "",
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        return ""

    def destroy(self, **kwargs: Any) -> None:
        """None"""

    def export_config(self, **kwargs: Any) -> str:
        return ""

    def export_config_and_config_id(self, **kwargs: Any) -> Tuple[str, int]:
        return "", 0

    def export_csv_entity_report(
        self,
        csv_column_list: str,
        flags: int = G2EngineFlags.G2_EXPORT_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> int:
        return 0

    def export_csv_entity_report_iterator(
        self,
        flags: int = G2EngineFlags.G2_EXPORT_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> Iterable[str]:
        return [""]

    def export_json_entity_report(
        self, flags: int = G2EngineFlags.G2_EXPORT_DEFAULT_FLAGS, **kwargs: Any
    ) -> int:
        return 0

    def export_json_entity_report_iterator(
        self,
        flags: int = G2EngineFlags.G2_EXPORT_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> Iterable[str]:
        return [""]

    def fetch_next(self, response_handle: int, **kwargs: Any) -> str:
        return ""

    def find_interesting_entities_by_entity_id(
        self, entity_id: int, flags: int = 0, **kwargs: Any
    ) -> str:
        return ""

    def find_interesting_entities_by_record_id(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_network_by_entity_id_v2(
        self,
        entity_list: Union[str, Dict[Any, Any]],
        max_degree: int,
        build_out_degree: int,
        max_entities: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_network_by_entity_id(
        self,
        entity_list: Union[str, Dict[Any, Any]],
        max_degree: int,
        build_out_degree: int,
        max_entities: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_network_by_record_id_v2(
        self,
        record_list: Union[str, Dict[Any, Any]],
        max_degree: int,
        build_out_degree: int,
        max_entities: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_network_by_record_id(
        self,
        record_list: Union[str, Dict[Any, Any]],
        max_degree: int,
        build_out_degree: int,
        max_entities: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_path_by_entity_id_v2(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_path_by_entity_id(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_path_by_record_id_v2(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_path_by_record_id(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_path_excluding_by_entity_id_v2(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        excluded_entities: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_path_excluding_by_entity_id(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        excluded_entities: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_path_excluding_by_record_id_v2(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        excluded_records: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_path_excluding_by_record_id(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        excluded_records: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_path_including_source_by_entity_id_v2(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        excluded_entities: Union[str, Dict[Any, Any]],
        required_dsrcs: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_path_including_source_by_entity_id(
        self,
        entity_id_1: int,
        entity_id_2: int,
        max_degree: int,
        excluded_entities: Union[str, Dict[Any, Any]],
        required_dsrcs: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_path_including_source_by_record_id_v2(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        excluded_records: Union[str, Dict[Any, Any]],
        required_dsrcs: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def find_path_including_source_by_record_id(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        max_degree: int,
        excluded_records: Union[str, Dict[Any, Any]],
        required_dsrcs: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_FIND_PATH_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def get_active_config_id(self, **kwargs: Any) -> int:
        return 0

    def get_entity_by_entity_id_v2(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def get_entity_by_entity_id(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def get_entity_by_record_id_v2(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def get_entity_by_record_id(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def get_record_v2(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_RECORD_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def get_record(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_RECORD_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def get_redo_record(self, **kwargs: Any) -> str:
        return ""

    def get_repository_last_modified_time(self, **kwargs: Any) -> int:
        return 0

    def get_virtual_entity_by_record_id_v2(
        self,
        record_list: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_HOW_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def get_virtual_entity_by_record_id(
        self,
        record_list: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_HOW_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def how_entity_by_entity_id_v2(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_HOW_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def how_entity_by_entity_id(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_HOW_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def init(
        self,
        module_name: str,
        ini_params: Union[str, Dict[Any, Any]],
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """None"""

    def init_with_config_id(
        self,
        module_name: str,
        ini_params: Union[str, Dict[Any, Any]],
        init_config_id: int,
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """None"""

    def prime_engine(self, **kwargs: Any) -> None:
        """None"""

    def process(self, record: Union[str, Dict[Any, Any]], **kwargs: Any) -> None:
        """None"""

    def process_with_info(
        self, record: Union[str, Dict[Any, Any]], flags: int, **kwargs: Any
    ) -> str:
        return ""

    def purge_repository(self, **kwargs: Any) -> None:
        """None"""

    def reevaluate_entity(self, entity_id: int, flags: int = 0, **kwargs: Any) -> None:
        """None"""

    def reevaluate_entity_with_info(
        self, entity_id: int, flags: int = 0, **kwargs: Any
    ) -> str:
        return ""

    def reevaluate_record(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = 0,
        **kwargs: Any,
    ) -> None:
        """None"""

    def reevaluate_record_with_info(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        return ""

    def reinit(self, init_config_id: int, **kwargs: Any) -> None:
        """None"""

    def replace_record(
        self,
        data_source_code: str,
        record_id: str,
        json_data: Union[str, Dict[Any, Any]],
        # TODO: load_id is no longer used, being removed from V4 C api?
        load_id: str = "",
        **kwargs: Any,
    ) -> None:
        """None"""

    def replace_record_with_info(
        self,
        data_source_code: str,
        record_id: str,
        json_data: Union[str, Dict[Any, Any]],
        # TODO: load_id is no longer used, being removed from V4 C api?
        load_id: str = "",
        flags: int = 0,
        **kwargs: Any,
    ) -> str:
        return ""

    def search_by_attributes_v2(
        self,
        json_data: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def search_by_attributes_v3(
        self,
        json_data: Union[str, Dict[Any, Any]],
        search_profile: str,
        flags: int = G2EngineFlags.G2_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def search_by_attributes(
        self,
        json_data: Union[str, Dict[Any, Any]],
        flags: int = G2EngineFlags.G2_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def stats(self, **kwargs: Any) -> str:
        return ""

    def why_entities_v2(
        self,
        entity_id_1: int,
        entity_id_2: int,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def why_entities(
        self,
        entity_id_1: int,
        entity_id_2: int,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def why_entity_by_entity_id_v2(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def why_entity_by_entity_id(
        self,
        entity_id: int,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def why_entity_by_record_id_v2(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def why_entity_by_record_id(
        self,
        data_source_code: str,
        record_id: str,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def why_record_in_entity(
        self,
        data_source_code: str,
        record_id: str,
        **kwargs: Any,
    ) -> str:
        return ""

    def why_record_in_entity_v2(
        self,
        data_source_code: str,
        record_id: str,
        flags: int,
        **kwargs: Any,
    ) -> str:
        return ""

    def why_records_v2(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""

    def why_records(
        self,
        data_source_code_1: str,
        record_id_1: str,
        data_source_code_2: str,
        record_id_2: str,
        flags: int = G2EngineFlags.G2_WHY_ENTITY_DEFAULT_FLAGS,
        **kwargs: Any,
    ) -> str:
        return ""


# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_add_record(g2_engine: g2engine_abstract.G2EngineAbstract) -> None:
    """Test G2Engine().add_record()."""
    g2_engine.add_record("", "", "")


def test_add_record_with_info(g2_engine: g2engine_abstract.G2EngineAbstract) -> None:
    """Test G2Engine().add_record_with_info()."""
    g2_engine.add_record_with_info("", "", "")


def test_close_export(g2_engine: g2engine_abstract.G2EngineAbstract) -> None:
    """Test G2Engine().close_export()."""
    g2_engine.close_export(0)


def test_count_redo_records(g2_engine: g2engine_abstract.G2EngineAbstract) -> None:
    """Test G2Engine().count_redo_records()."""
    g2_engine.count_redo_records()


def test_delete_record(g2_engine: g2engine_abstract.G2EngineAbstract) -> None:
    """Test G2Engine().delete_record()."""
    g2_engine.delete_record("", "")


def test_delete_record_with_info(g2_engine: g2engine_abstract.G2EngineAbstract) -> None:
    """Test G2Engine().delete_record_with_info()."""
    g2_engine.delete_record_with_info("", "")


def test_destroy(g2_engine: g2engine_abstract.G2EngineAbstract) -> None:
    """Test G2Engine().destroy()."""
    g2_engine.destroy()


def test_export_config(g2_engine: g2engine_abstract.G2EngineAbstract) -> None:
    """Test G2Engine().export_config()."""
    g2_engine.export_config()


def test_export_config_and_config_id(
    g2_engine: g2engine_abstract.G2EngineAbstract,
) -> None:
    """Test G2Engine().export_config_and_config_id()."""
    g2_engine.export_config_and_config_id()


def test_export_csv_entity_report(
    g2_engine: g2engine_abstract.G2EngineAbstract,
) -> None:
    """Test G2Engine().export_csv_entity_report()."""
    g2_engine.export_csv_entity_report("")


def test_export_csv_entity_report_iterator(
    g2_engine: g2engine_abstract.G2EngineAbstract,
) -> None:
    """Test G2Engine().export_csv_entity_report_iterator()."""
    g2_engine.export_csv_entity_report_iterator()
