#! /usr/bin/env python3

"""
TODO: szconfigmanager_test.py
"""

# pylint: disable=E1101

from typing import Any, Dict, Union

import pytest

from senzing_abstract import szconfigmanager_abstract

# -----------------------------------------------------------------------------
# SzConfig fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_configmanager", scope="module")  # type: ignore[misc]
def szconfigmanager_fixture() -> szconfigmanager_abstract.SzConfigManagerAbstract:
    """
    Object under test.
    """

    return SzConfigManagerTest()


# -----------------------------------------------------------------------------
# SzConfigManagerTest class
# -----------------------------------------------------------------------------


class SzConfigManagerTest(szconfigmanager_abstract.SzConfigManagerAbstract):
    """
    G2 configmgr module access library.
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

    def destroy(self, **kwargs: Any) -> None:
        """None"""

    def get_config(self, config_id: int, **kwargs: Any) -> str:
        return ""

    def get_config_list(self, **kwargs: Any) -> str:
        return ""

    def get_default_config_id(self, **kwargs: Any) -> int:
        return 0

    def initialize(
        self,
        instance_name: str,
        settings: Union[str, Dict[Any, Any]],
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """None"""

    def replace_default_config_id(
        self, current_default_config_id: int, new_default_config_id: int, **kwargs: Any
    ) -> None:
        """None"""

    def set_default_config_id(self, config_id: int, **kwargs: Any) -> None:
        """None"""


# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_add_config(
    sz_configmanager: szconfigmanager_abstract.SzConfigManagerAbstract,
) -> None:
    """Test SzConfigManager().add_config()."""
    sz_configmanager.add_config("", "")


def test_destroy(
    sz_configmanager: szconfigmanager_abstract.SzConfigManagerAbstract,
) -> None:
    """Test SzConfigManager().destroy()."""
    sz_configmanager.destroy()


def test_get_config(
    sz_configmanager: szconfigmanager_abstract.SzConfigManagerAbstract,
) -> None:
    """Test SzConfigManager().get_config()."""
    sz_configmanager.get_config(0)


def test_get_config_list(
    sz_configmanager: szconfigmanager_abstract.SzConfigManagerAbstract,
) -> None:
    """Test SzConfigManager().get_config_list()."""
    sz_configmanager.get_config_list()


def test_get_default_config_id(
    sz_configmanager: szconfigmanager_abstract.SzConfigManagerAbstract,
) -> None:
    """Test SzConfigManager().get_default_config_id()."""
    sz_configmanager.get_default_config_id()


def test_initialize(
    sz_configmanager: szconfigmanager_abstract.SzConfigManagerAbstract,
) -> None:
    """Test SzConfigManager().initialize()."""
    sz_configmanager.initialize("", "")


def test_replace_default_config_id(
    sz_configmanager: szconfigmanager_abstract.SzConfigManagerAbstract,
) -> None:
    """Test SzConfigManager().replace_default_config_id()."""
    sz_configmanager.replace_default_config_id(0, 0)


def test_set_default_config_id(
    sz_configmanager: szconfigmanager_abstract.SzConfigManagerAbstract,
) -> None:
    """Test SzConfigManager().set_default_config_id()."""
    sz_configmanager.set_default_config_id(0)
