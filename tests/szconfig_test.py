#! /usr/bin/env python3

"""
TODO: szconfig_test.py
"""

# pylint: disable=E1101

from typing import Any, Dict, Optional, Union

import pytest

from senzing_abstract import szconfig_abstract

# -----------------------------------------------------------------------------
# szConfig fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_config", scope="module")
def szconfig_fixture() -> szconfig_abstract.SzConfigAbstract:
    """
    Object under test.
    """

    return SzConfigTest()


# -----------------------------------------------------------------------------
# SzConfigTest class
# -----------------------------------------------------------------------------


class SzConfigTest(szconfig_abstract.SzConfigAbstract):
    """
    SzConfig module access library.
    """

    # -------------------------------------------------------------------------
    # SzConfig methods
    # -------------------------------------------------------------------------

    def add_data_source(
        self,
        config_handle: int,
        data_source_code: str,
        **kwargs: Any,
    ) -> str:
        return ""

    def close_config(self, config_handle: int, **kwargs: Any) -> None:
        """None"""

    def create_config(self, **kwargs: Any) -> int:
        return 0

    def delete_data_source(
        self,
        config_handle: int,
        data_source_code: str,
        **kwargs: Any,
    ) -> None:
        """None"""

    def destroy(self, **kwargs: Any) -> None:
        """None"""

    def export_config(self, config_handle: int, **kwargs: Any) -> str:
        return ""

    def get_data_sources(self, config_handle: int, **kwargs: Any) -> str:
        return ""

    def import_config(
        self, config_definition: Union[str, Dict[Any, Any]], **kwargs: Any
    ) -> int:
        return 0

    def initialize(
        self,
        instance_name: str,
        settings: Union[str, Dict[Any, Any]],
        verbose_logging: Optional[int] = 0,
        **kwargs: Any,
    ) -> None:
        """None"""


# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_add_data_source(sz_config: szconfig_abstract.SzConfigAbstract) -> None:
    """Test SzConfig().add_data_source()."""
    sz_config.add_data_source(0, "")


def test_close_config(sz_config: szconfig_abstract.SzConfigAbstract) -> None:
    """Test SzConfig().close_config()."""
    sz_config.close_config(0)


def test_create_config(sz_config: szconfig_abstract.SzConfigAbstract) -> None:
    """Test SzConfig().create_config()."""
    sz_config.create_config()


def test_delete_data_source(sz_config: szconfig_abstract.SzConfigAbstract) -> None:
    """Test SzConfig().delete_data_source()."""
    sz_config.delete_data_source(0, "")


def test_destroy(sz_config: szconfig_abstract.SzConfigAbstract) -> None:
    """Test SzConfig().destroy()."""
    sz_config.destroy()


def test_export_config(sz_config: szconfig_abstract.SzConfigAbstract) -> None:
    """Test SzConfig().export_config()."""
    sz_config.export_config(0)


def test_get_data_sources(sz_config: szconfig_abstract.SzConfigAbstract) -> None:
    """Test SzConfig().get_data_sources()."""
    sz_config.get_data_sources(0)


def test_import_config(sz_config: szconfig_abstract.SzConfigAbstract) -> None:
    """Test SzConfig().import_config()."""
    sz_config.import_config("")


def test_initialize(sz_config: szconfig_abstract.SzConfigAbstract) -> None:
    """Test SzConfig().initialize()."""
    sz_config.initialize("", "")
