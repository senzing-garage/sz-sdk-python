"""
szdiagnostic_test.py
"""

import pytest

from senzing import SzDiagnostic
from senzing_mock import SzDiagnosticMock

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_check_repository_performance(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnostic.check_repository_performance()."""
    sz_diagnostic.check_repository_performance(0)


def test_get_repository_info(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnostic.get_repository_info()."""
    sz_diagnostic.get_repository_info()


def test_get_feature(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnostic.get_feature()."""
    sz_diagnostic.get_feature(0)


def test_help_1(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnostic.help()."""
    sz_diagnostic.help()


def test_help_2(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnostic.help(...)."""
    sz_diagnostic.help("check_repository_performance")


# -----------------------------------------------------------------------------
# Unique testcases
# -----------------------------------------------------------------------------

# def test_initialize(sz_diagnostic: SzDiagnostic) -> None:
#     """Test SzDiagnostic.initialize()."""
#     sz_diagnostic.initialize("", "")


# def test_destroy(sz_diagnostic: SzDiagnostic) -> None:
#     """Test SzDiagnostic.destroy()."""
#     sz_diagnostic.destroy()


def test_purge_repository(sz_diagnostic: SzDiagnostic) -> None:
    """Test SzDiagnostic.purge_repository()."""
    sz_diagnostic.purge_repository()


# -----------------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_diagnostic", scope="module")
def szdiagnostic_fixture() -> SzDiagnostic:
    """
    Object under test.
    """

    return SzDiagnosticMock()
