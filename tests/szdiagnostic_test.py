#! /usr/bin/env python3

"""
TODO: szdiagnostic_test.py
"""

import pytest

from senzing import SzDiagnostic
from senzing_mock import SzDiagnosticMock

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


def test_help_1(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnosic().help()."""
    sz_diagnostic.help()


def test_help_2(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnosic().help(...)."""
    sz_diagnostic.help("check_datastore_performance")


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

    return SzDiagnosticMock()
