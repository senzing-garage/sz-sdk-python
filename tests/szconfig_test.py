#! /usr/bin/env python3

"""
TODO: szconfig_test.py
"""


import pytest

from senzing import SzConfig

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_add_data_source(sz_config: SzConfig) -> None:
    """Test SzConfig.add_data_source()."""
    sz_config.add_data_source("")


def test_delete_data_source(sz_config: SzConfig) -> None:
    """Test SzConfig.delete_data_source()."""
    sz_config.delete_data_source("")


def test_export(sz_config: SzConfig) -> None:
    """Test SzConfig.export()."""
    sz_config.export()


def test_get_data_sources(sz_config: SzConfig) -> None:
    """Test SzConfig.get_data_sources()."""
    sz_config.get_data_sources()


# -----------------------------------------------------------------------------
# szConfig fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_config", scope="module")
def szconfig_fixture() -> SzConfig:
    """
    Object under test.
    """

    return SzConfigTest()


# -----------------------------------------------------------------------------
# SzConfigTest class
# -----------------------------------------------------------------------------


class SzConfigTest(SzConfig):
    """
    SzConfig module access library.
    """

    # -------------------------------------------------------------------------
    # SzConfig methods
    # -------------------------------------------------------------------------

    def add_data_source(
        self,
        data_source_code: str,
    ) -> str:
        return ""

    def delete_data_source(
        self,
        data_source_code: str,
    ) -> str:
        return ""

    def export(self) -> str:
        return ""

    def get_data_sources(self) -> str:
        return ""
