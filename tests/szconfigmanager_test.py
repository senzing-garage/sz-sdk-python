#! /usr/bin/env python3

"""
TODO: szconfigmanager_test.py
"""

from typing import Any, Dict, Union

import pytest

from senzing import SzConfig, SzConfigManager

from . import SzConfigTest

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_create_config_from_config_id(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.create_config_from_config_id()."""
    sz_configmanager.create_config_from_config_id(0)


def test_create_config_from_config_string(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.create_config_from_config_string()."""
    sz_configmanager.create_config_from_string("")


def test_create_config_from_config_template(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.create_config_from_config_string()."""
    sz_configmanager.create_config_from_template()


def test_get_configs(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.get_configs()."""
    sz_configmanager.get_configs()


def test_get_default_config_id(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.get_default_config_id()."""
    sz_configmanager.get_default_config_id()


def test_register_config(sz_configmanager: SzConfigManager) -> None:
    """Test SzConfigManager.add_config()."""
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
# SzConfig fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_configmanager", scope="module")
def szconfigmanager_fixture() -> SzConfigManager:
    """
    Object under test.
    """

    return SzConfigManagerTest()


# -----------------------------------------------------------------------------
# SzConfigManagerTest class
# -----------------------------------------------------------------------------


class SzConfigManagerTest(SzConfigManager):
    """
    SzConfigManager module access library.
    """

    # -------------------------------------------------------------------------
    # SzConfigManager methods
    # -------------------------------------------------------------------------

    def create_config_from_config_id(self, config_id: int) -> SzConfig:
        return SzConfigTest()

    def create_config_from_string(self, config_definition: str) -> SzConfig:
        return SzConfigTest()

    def create_config_from_template(self) -> SzConfig:
        return SzConfigTest()

    def get_configs(self) -> str:
        return ""

    def get_default_config_id(self) -> int:
        return 0

    def register_config(
        self,
        config_definition: Union[str, Dict[Any, Any]],
        config_comment: str,
    ) -> int:
        return 0

    def replace_default_config_id(
        self, current_default_config_id: int, new_default_config_id: int, **kwargs: Any
    ) -> None:
        """None"""

    def set_default_config(self, config_definition: str, config_comment: str) -> int:
        return 0

    def set_default_config_id(self, config_id: int) -> None:
        """None"""
