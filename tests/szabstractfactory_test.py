#! /usr/bin/env python3

"""
TODO: szabstractfactory_test.py
"""


import pytest

from senzing import (
    SzAbstractFactory,
    SzConfigManager,
    SzDiagnostic,
    SzEngine,
    SzProduct,
)
from senzing_mock import SzAbstractFactoryMock

# -----------------------------------------------------------------------------
# SzAbstractFactory testcases
# -----------------------------------------------------------------------------


def test_create_configmanager(szabstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.create_configmanager()."""
    actual = szabstractfactory.create_configmanager()
    assert isinstance(actual, SzConfigManager)


def test_create_diagnostic(szabstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.create_diagnostic()."""
    actual = szabstractfactory.create_diagnostic()
    assert isinstance(actual, SzDiagnostic)


def test_create_engine(szabstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.create_engine()."""
    actual = szabstractfactory.create_engine()
    assert isinstance(actual, SzEngine)


def test_create_product(szabstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.create_product()."""
    actual = szabstractfactory.create_product()
    assert isinstance(actual, SzProduct)


def test_help_1(szabstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory().help()."""
    szabstractfactory.help()


def test_help_2(szabstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory().help(...)."""
    szabstractfactory.help("create_configmanager")


def test_reinitialize(szabstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.reinitialize()."""
    szabstractfactory.reinitialize(0)


# -----------------------------------------------------------------------------
# SzAbstractFactory fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="szabstractfactory", scope="module")
def szabstractfactory_fixture() -> SzAbstractFactory:
    """
    Single sz_abstractfactory object to use for all tests.
    """
    return SzAbstractFactoryMock()
