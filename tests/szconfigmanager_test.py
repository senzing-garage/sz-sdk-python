#! /usr/bin/env python3

"""
TODO: szconfigmanager_test.py
"""

from typing import Any, Dict, Union

import pytest

from senzing import SzConfigManagerAbstract

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_add_config(sz_configmanager: SzConfigManagerAbstract) -> None:
    """Test SzConfigManager().add_config()."""
    sz_configmanager.add_config("", "")


# def test_destroy(sz_configmanager: SzConfigManagerAbstract) -> None:
#     """Test SzConfigManager().destroy()."""
#     sz_configmanager.destroy()


def test_get_config(sz_configmanager: SzConfigManagerAbstract) -> None:
    """Test SzConfigManager().get_config()."""
    sz_configmanager.get_config(0)


def test_get_configs(sz_configmanager: SzConfigManagerAbstract) -> None:
    """Test SzConfigManager().get_configs()."""
    sz_configmanager.get_configs()


def test_get_default_config_id(sz_configmanager: SzConfigManagerAbstract) -> None:
    """Test SzConfigManager().get_default_config_id()."""
    sz_configmanager.get_default_config_id()


# def test_initialize(sz_configmanager: SzConfigManagerAbstract) -> None:
#     """Test SzConfigManager().initialize()."""
#     sz_configmanager.initialize("", "")


def test_replace_default_config_id(sz_configmanager: SzConfigManagerAbstract) -> None:
    """Test SzConfigManager().replace_default_config_id()."""
    sz_configmanager.replace_default_config_id(0, 0)


def test_set_default_config_id(sz_configmanager: SzConfigManagerAbstract) -> None:
    """Test SzConfigManager().set_default_config_id()."""
    sz_configmanager.set_default_config_id(0)


# -----------------------------------------------------------------------------
# SzConfig fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_configmanager", scope="module")
def szconfigmanager_fixture() -> SzConfigManagerAbstract:
    """
    Object under test.
    """

    return SzConfigManagerTest()


# -----------------------------------------------------------------------------
# SzConfigManagerTest class
# -----------------------------------------------------------------------------


class SzConfigManagerTest(SzConfigManagerAbstract):
    """
    SzConfigManager module access library.
    """

    # -------------------------------------------------------------------------
    # SzConfigManager methods
    # -------------------------------------------------------------------------

    def add_config(
        self,
        config_definition: Union[str, Dict[Any, Any]],
        config_comment: str,
        **kwargs: Any,
    ) -> int:
        return 0

    def get_config(self, config_id: int, **kwargs: Any) -> str:
        return ""

    def get_configs(self, **kwargs: Any) -> str:
        return ""

    def get_default_config_id(self, **kwargs: Any) -> int:
        return 0

    def replace_default_config_id(
        self, current_default_config_id: int, new_default_config_id: int, **kwargs: Any
    ) -> None:
        """None"""

    def set_default_config_id(self, config_id: int, **kwargs: Any) -> None:
        """None"""
