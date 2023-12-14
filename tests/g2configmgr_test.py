#! /usr/bin/env python3

"""
TODO: g2configmgr_test.py
"""

# pylint: disable=E1101

from typing import Any, Dict, Union

import pytest

from senzing_abstract import g2configmgr_abstract

# -----------------------------------------------------------------------------
# G2Config fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="g2_configmgr", scope="module")  # type: ignore[misc]
def g2configmgr_fixture() -> g2configmgr_abstract.G2ConfigMgrAbstract:
    """
    Object under test.
    """

    return G2ConfigMgrTest()


# -----------------------------------------------------------------------------
# G2ConfigTest class
# -----------------------------------------------------------------------------


class G2ConfigMgrTest(g2configmgr_abstract.G2ConfigMgrAbstract):
    """
    G2 configmgr module access library.
    """

    # -------------------------------------------------------------------------
    # G2ConfigMgr methods
    # -------------------------------------------------------------------------

    def add_config(
        self,
        config_str: Union[str, Dict[Any, Any]],
        config_comments: str,
        *args: Any,
        **kwargs: Any,
    ) -> int:
        return 0

    def destroy(self, *args: Any, **kwargs: Any) -> None:
        """None"""

    def get_config(self, config_id: int, *args: Any, **kwargs: Any) -> str:
        return ""

    def get_config_list(self, *args: Any, **kwargs: Any) -> str:
        return ""

    def get_default_config_id(self, *args: Any, **kwargs: Any) -> int:
        return 0

    def init(
        self,
        module_name: str,
        ini_params: Union[str, Dict[Any, Any]],
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """None"""

    def replace_default_config_id(
        self, old_config_id: int, new_config_id: int, *args: Any, **kwargs: Any
    ) -> None:
        """None"""

    def set_default_config_id(self, config_id: int, *args: Any, **kwargs: Any) -> None:
        """None"""


# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_add_config(g2_configmgr: g2configmgr_abstract.G2ConfigMgrAbstract) -> None:
    """Test G2ConfigMgr().add_config()."""
    g2_configmgr.add_config("", "")


def test_destroy(g2_configmgr: g2configmgr_abstract.G2ConfigMgrAbstract) -> None:
    """Test G2ConfigMgr().destroy()."""
    g2_configmgr.destroy()


def test_get_config(g2_configmgr: g2configmgr_abstract.G2ConfigMgrAbstract) -> None:
    """Test G2ConfigMgr().get_config()."""
    g2_configmgr.get_config(0)


def test_get_config_list(
    g2_configmgr: g2configmgr_abstract.G2ConfigMgrAbstract,
) -> None:
    """Test G2ConfigMgr().get_config_list()."""
    g2_configmgr.get_config_list()


def test_get_default_config_id(
    g2_configmgr: g2configmgr_abstract.G2ConfigMgrAbstract,
) -> None:
    """Test G2ConfigMgr().get_default_config_id()."""
    g2_configmgr.get_default_config_id()


def test_init(
    g2_configmgr: g2configmgr_abstract.G2ConfigMgrAbstract,
) -> None:
    """Test G2ConfigMgr().init()."""
    g2_configmgr.init("", "")


def test_replace_default_config_id(
    g2_configmgr: g2configmgr_abstract.G2ConfigMgrAbstract,
) -> None:
    """Test G2ConfigMgr().replace_default_config_id()."""
    g2_configmgr.replace_default_config_id(0, 0)


def test_set_default_config_id(
    g2_configmgr: g2configmgr_abstract.G2ConfigMgrAbstract,
) -> None:
    """Test G2ConfigMgr().set_default_config_id()."""
    g2_configmgr.set_default_config_id(0)
