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


def test_register_data_source(sz_config: SzConfig) -> None:
    """Test SzConfig.register_data_source()."""
    sz_config.register_data_source("")


def test_unregister_data_source(sz_config: SzConfig) -> None:
    """Test SzConfig.unregister_data_source()."""
    sz_config.unregister_data_source("")


def test_export(sz_config: SzConfig) -> None:
    """Test SzConfig.export()."""
    sz_config.export()


def test_get_data_source_registry(sz_config: SzConfig) -> None:
    """Test SzConfig.get_data_source_registry()."""
    sz_config.get_data_source_registry()


def test_help_1(sz_config: SzConfig) -> None:
    """Test SzConfig.help()."""
    sz_config.help()


def test_help_2(sz_config: SzConfig) -> None:
    """Test SzConfig.help(...)."""
    sz_config.help("register_data_source")


# -----------------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_config", scope="module")
def szconfig_fixture() -> SzConfig:
    """
    Object under test.
    """

    return SzConfigMock()
