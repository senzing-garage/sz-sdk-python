#! /usr/bin/env python3

"""
TODO: g2diagnostic_test.py
"""

# pylint: disable=E1101

from typing import Any, Dict, Union

import pytest

from senzing_abstract import g2diagnostic_abstract

# -----------------------------------------------------------------------------
# G2Config fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="g2_diagnostic", scope="module")  # type: ignore[misc]
def g2diagnostic_fixture() -> g2diagnostic_abstract.G2DiagnosticAbstract:
    """
    Object under test.
    """

    return G2DiagnosticTest()


# -----------------------------------------------------------------------------
# G2ConfigTest class
# -----------------------------------------------------------------------------


class G2DiagnosticTest(g2diagnostic_abstract.G2DiagnosticAbstract):
    """
    G2 diagnostic module access library.
    """

    # -------------------------------------------------------------------------
    # G2Diagnostic methods
    # -------------------------------------------------------------------------

    def check_db_perf(self, seconds_to_run: int, *args: Any, **kwargs: Any) -> str:
        return ""

    def destroy(self, *args: Any, **kwargs: Any) -> None:
        """None"""

    def get_available_memory(self, *args: Any, **kwargs: Any) -> int:
        return 0

    def get_db_info(self, *args: Any, **kwargs: Any) -> str:
        return ""

    def get_logical_cores(self, *args: Any, **kwargs: Any) -> int:
        return 0

    def get_physical_cores(self, *args: Any, **kwargs: Any) -> int:
        return 0

    def get_total_system_memory(self, *args: Any, **kwargs: Any) -> int:
        return 0

    def init(
        self,
        module_name: str,
        ini_params: Union[str, Dict[Any, Any]],
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """None"""

    def init_with_config_id(
        self,
        module_name: str,
        ini_params: Union[str, Dict[Any, Any]],
        init_config_id: int,
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """None"""

    def reinit(self, init_config_id: int, *args: Any, **kwargs: Any) -> None:
        """None"""


# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_check_db_perf(
    g2_diagnostic: g2diagnostic_abstract.G2DiagnosticAbstract,
) -> None:
    """Test G2Config().check_db_perf()."""
    g2_diagnostic.check_db_perf(0)


def test_destroy(
    g2_diagnostic: g2diagnostic_abstract.G2DiagnosticAbstract,
) -> None:
    """Test G2Config().destroy()."""
    g2_diagnostic.destroy()


def test_get_available_memory(
    g2_diagnostic: g2diagnostic_abstract.G2DiagnosticAbstract,
) -> None:
    """Test G2Config().get_available_memory()."""
    g2_diagnostic.get_available_memory()


def test_get_db_info(
    g2_diagnostic: g2diagnostic_abstract.G2DiagnosticAbstract,
) -> None:
    """Test G2Config().get_db_info()."""
    g2_diagnostic.get_db_info()


def test_get_logical_cores(
    g2_diagnostic: g2diagnostic_abstract.G2DiagnosticAbstract,
) -> None:
    """Test G2Config().get_logical_cores()."""
    g2_diagnostic.get_logical_cores()


def test_get_physical_cores(
    g2_diagnostic: g2diagnostic_abstract.G2DiagnosticAbstract,
) -> None:
    """Test G2Config().get_physical_cores()."""
    g2_diagnostic.get_physical_cores()


def test_get_total_system_memory(
    g2_diagnostic: g2diagnostic_abstract.G2DiagnosticAbstract,
) -> None:
    """Test G2Config().get_total_system_memory()."""
    g2_diagnostic.get_total_system_memory()


def test_init(
    g2_diagnostic: g2diagnostic_abstract.G2DiagnosticAbstract,
) -> None:
    """Test G2Config().init()."""
    g2_diagnostic.init("", "")


def test_init_with_config_id(
    g2_diagnostic: g2diagnostic_abstract.G2DiagnosticAbstract,
) -> None:
    """Test G2Config().init_with_config_id()."""
    g2_diagnostic.init_with_config_id("", "", 0)


def test_reinit(
    g2_diagnostic: g2diagnostic_abstract.G2DiagnosticAbstract,
) -> None:
    """Test G2Config().reinit()."""
    g2_diagnostic.reinit(0)
