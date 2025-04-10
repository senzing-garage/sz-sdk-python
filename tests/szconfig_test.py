#! /usr/bin/env python3

"""
TODO: szconfig_test.py
"""


import pytest

from senzing import SzConfig
from senzing_mock import SzConfigMock

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


def test_help_1(sz_config: SzConfig) -> None:
    """Test SzConfig().help()."""
    sz_config.help()


def test_help_2(sz_config: SzConfig) -> None:
    """Test SzConfig().help(...)."""
    sz_config.help("add_data_source")


# -----------------------------------------------------------------------------
# szConfig fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_config", scope="module")
def szconfig_fixture() -> SzConfig:
    """
    Object under test.
    """

    return SzConfigMock()
