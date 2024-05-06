#! /usr/bin/env python3

"""
TODO: szdiagnostic_test.py
"""

# pylint: disable=E1101

from typing import Any, Dict, Optional, Union

import pytest

from senzing_abstract import szdiagnostic_abstract

# -----------------------------------------------------------------------------
# SzDiagnostic fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_diagnostic", scope="module")
def szdiagnostic_fixture() -> szdiagnostic_abstract.SzDiagnosticAbstract:
    """
    Object under test.
    """

    return SzDiagnosticTest()


# -----------------------------------------------------------------------------
# SzDiagnosticTest class
# -----------------------------------------------------------------------------


class SzDiagnosticTest(szdiagnostic_abstract.SzDiagnosticAbstract):
    """
    SzDiagnostic module access library.
    """

    # -------------------------------------------------------------------------
    # SzDiagnostic methods
    # -------------------------------------------------------------------------

    def check_datastore_performance(self, seconds_to_run: int, **kwargs: Any) -> str:
        return ""

    def destroy(self, **kwargs: Any) -> None:
        """None"""

    def get_datastore_info(self, **kwargs: Any) -> str:
        return ""

    def get_feature(self, feature_id: int, **kwargs: Any) -> str:
        return ""

    def initialize(
        self,
        instance_name: str,
        settings: Union[str, Dict[Any, Any]],
        config_id: Optional[int] = None,
        verbose_logging: Optional[int] = 0,
        **kwargs: Any,
    ) -> None:
        """None"""

    def purge_repository(self, **kwargs: Any) -> None:
        """None"""

    def reinitialize(self, config_id: int, **kwargs: Any) -> None:
        """None"""


# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_check_datastore_performance(
    sz_diagnostic: szdiagnostic_abstract.SzDiagnosticAbstract,
) -> None:
    """Test SzDiagnosic().check_datastore_performance()."""
    sz_diagnostic.check_datastore_performance(0)


def test_destroy(
    sz_diagnostic: szdiagnostic_abstract.SzDiagnosticAbstract,
) -> None:
    """Test SzDiagnosic().destroy()."""
    sz_diagnostic.destroy()


def test_get_datastore_info(
    sz_diagnostic: szdiagnostic_abstract.SzDiagnosticAbstract,
) -> None:
    """Test SzDiagnosic().get_datastore_info()."""
    sz_diagnostic.get_datastore_info()


def test_get_feature(
    sz_diagnostic: szdiagnostic_abstract.SzDiagnosticAbstract,
) -> None:
    """Test SzDiagnosic().get_datastore_info()."""
    sz_diagnostic.get_feature(0)


def test_initialize(
    sz_diagnostic: szdiagnostic_abstract.SzDiagnosticAbstract,
) -> None:
    """Test SzDiagnosic().initialize()."""
    sz_diagnostic.initialize("", "")


def test_purge_repository(
    sz_diagnostic: szdiagnostic_abstract.SzDiagnosticAbstract,
) -> None:
    """Test SzDiagnosic().purge_repository()."""
    sz_diagnostic.purge_repository()


def test_reinitialize(
    sz_diagnostic: szdiagnostic_abstract.SzDiagnosticAbstract,
) -> None:
    """Test SzDiagnosic().reinitialize()."""
    sz_diagnostic.reinitialize(0)
