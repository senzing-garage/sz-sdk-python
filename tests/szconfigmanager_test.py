#! /usr/bin/env python3

"""
TODO: szconfigmanager_test.py
"""


import pytest

from senzing import SzConfigManager
from senzing_mock import SzConfigManagerMock

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_create_config_from_config_id(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.create_config_from_config_id()."""
    sz_configmanager.create_config_from_config_id(0)


def test_create_config_from_string(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.create_config_from_string()."""
    sz_configmanager.create_config_from_string("")


def test_create_config_from_template(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.create_config_from_template()."""
    sz_configmanager.create_config_from_template()


def test_get_configs(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.get_configs()."""
    sz_configmanager.get_configs()


def test_get_default_config_id(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.get_default_config_id()."""
    sz_configmanager.get_default_config_id()


def test_help_1(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.help()."""
    sz_configmanager.help()


def test_help_2(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.help(...)."""
    sz_configmanager.help("register_config")


def test_register_config(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.register_config()."""
    sz_configmanager.register_config("", "")


def test_replace_default_config_id(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.replace_default_config_id()."""
    sz_configmanager.replace_default_config_id(0, 0)


def test_set_default_config(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.set_default_config()."""
    sz_configmanager.set_default_config("", "")


def test_set_default_config_id(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.set_default_config_id()."""
    sz_configmanager.set_default_config_id(0)


# -----------------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_configmanager", scope="module")
def szconfigmanager_fixture() -> SzConfigManager:
    """
    Object under test.
    """

    return SzConfigManagerMock()
