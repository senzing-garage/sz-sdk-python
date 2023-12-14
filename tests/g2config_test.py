#! /usr/bin/env python3

"""
TODO: g2config_test.py
"""

# pylint: disable=E1101

from typing import Any, Dict, Union

import pytest

from senzing_abstract import g2config_abstract

# -----------------------------------------------------------------------------
# G2Config fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="g2_config", scope="module")  # type: ignore[misc]
def g2config_fixture() -> g2config_abstract.G2ConfigAbstract:
    """
    Object under test.
    """

    return G2ConfigTest()


# -----------------------------------------------------------------------------
# G2ConfigTest class
# -----------------------------------------------------------------------------


class G2ConfigTest(g2config_abstract.G2ConfigAbstract):
    """
    G2 config module access library over gRPC.
    """

    # -------------------------------------------------------------------------
    # G2Config methods
    # -------------------------------------------------------------------------

    def add_data_source(
        self,
        config_handle: int,
        input_json: Union[str, Dict[Any, Any]],
        *args: Any,
        **kwargs: Any,
    ) -> str:
        return ""

    def close(self, config_handle: int, *args: Any, **kwargs: Any) -> None:
        """Null method"""

    def create(self, *args: Any, **kwargs: Any) -> int:
        return 0

    def delete_data_source(
        self,
        config_handle: int,
        input_json: Union[str, Dict[Any, Any]],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Null method"""

    def destroy(self, *args: Any, **kwargs: Any) -> None:
        """Null method"""

    def init(
        self,
        module_name: str,
        ini_params: Union[str, Dict[Any, Any]],
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """Null method"""

    def list_data_sources(self, config_handle: int, *args: Any, **kwargs: Any) -> str:
        return ""

    def load(
        self, json_config: Union[str, Dict[Any, Any]], *args: Any, **kwargs: Any
    ) -> int:
        return 0

    def save(self, config_handle: int, *args: Any, **kwargs: Any) -> str:
        return ""


# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_add_data_source(g2_config: g2config_abstract.G2ConfigAbstract) -> None:
    """Test G2Config().add_data_source()."""
    g2_config.add_data_source(0, "")


def test_close(g2_config: g2config_abstract.G2ConfigAbstract) -> None:
    """Test G2Config().close()."""
    g2_config.close(0, "")


def test_create(g2_config: g2config_abstract.G2ConfigAbstract) -> None:
    """Test G2Config().create()."""
    g2_config.create()


def test_delete_data_source(g2_config: g2config_abstract.G2ConfigAbstract) -> None:
    """Test G2Config().delete_data_source()."""
    g2_config.delete_data_source(0, "")


def test_destroy(g2_config: g2config_abstract.G2ConfigAbstract) -> None:
    """Test G2Config().destroy()."""
    g2_config.destroy(0, "")


def test_init(g2_config: g2config_abstract.G2ConfigAbstract) -> None:
    """Test G2Config().init()."""
    g2_config.init("", "")


def test_list_data_sources(g2_config: g2config_abstract.G2ConfigAbstract) -> None:
    """Test G2Config().list_data_sources()."""
    g2_config.list_data_sources(0)


def test_load(g2_config: g2config_abstract.G2ConfigAbstract) -> None:
    """Test G2Config().load()."""
    g2_config.load("")


def test_save(g2_config: g2config_abstract.G2ConfigAbstract) -> None:
    """Test G2Config().save()."""
    g2_config.save(0)
