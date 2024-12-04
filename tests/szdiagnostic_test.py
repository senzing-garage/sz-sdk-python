#! /usr/bin/env python3

"""
TODO: szdiagnostic_test.py
"""


import pytest

from senzing import SzDiagnostic

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_check_datastore_performance(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnosic().check_datastore_performance()."""
    sz_diagnostic.check_datastore_performance(0)


# def test_destroy(sz_diagnostic: SzDiagnostic) -> None:
#     """Test SzDiagnosic().destroy()."""
#     sz_diagnostic.destroy()


def test_get_datastore_info(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnosic().get_datastore_info()."""
    sz_diagnostic.get_datastore_info()


def test_get_feature(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnosic().get_datastore_info()."""
    sz_diagnostic.get_feature(0)


# def test_initialize(sz_diagnostic: SzDiagnostic) -> None:
#     """Test SzDiagnosic().initialize()."""
#     sz_diagnostic.initialize("", "")


def test_purge_repository(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnosic().purge_repository()."""
    sz_diagnostic.purge_repository()


# -----------------------------------------------------------------------------
# SzDiagnostic fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_diagnostic", scope="module")
def szdiagnostic_fixture() -> SzDiagnostic:
    """
    Object under test.
    """

    return SzDiagnosticTest()


# -----------------------------------------------------------------------------
# SzDiagnosticTest class
# -----------------------------------------------------------------------------


class SzDiagnosticTest(SzDiagnostic):
    """
    SzDiagnostic module access library.
    """

    # -------------------------------------------------------------------------
    # SzDiagnostic methods
    # -------------------------------------------------------------------------

    def check_datastore_performance(self, seconds_to_run: int) -> str:
        return ""

    def get_datastore_info(self) -> str:
        return ""

    def get_feature(self, feature_id: int) -> str:
        return ""

    def purge_repository(self) -> None:
        """None"""
