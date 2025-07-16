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
# Test cases
# -----------------------------------------------------------------------------


def test_create_configmanager(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.create_configmanager()."""
    actual = sz_abstractfactory.create_configmanager()
    assert isinstance(actual, SzConfigManager)


def test_create_diagnostic(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.create_diagnostic()."""
    actual = sz_abstractfactory.create_diagnostic()
    assert isinstance(actual, SzDiagnostic)


def test_create_engine(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.create_engine()."""
    actual = sz_abstractfactory.create_engine()
    assert isinstance(actual, SzEngine)


def test_create_product(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.create_product()."""
    actual = sz_abstractfactory.create_product()
    assert isinstance(actual, SzProduct)


def test_help_1(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.help()."""
    sz_abstractfactory.help()


def test_help_2(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.help(...)."""
    sz_abstractfactory.help("create_configmanager")


def test_reinitialize(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.reinitialize()."""
    sz_abstractfactory.reinitialize(0)


def test_destroy(sz_abstractfactory: SzAbstractFactory) -> None:
    """Test SzAbstractFactory.test_destroy()."""
    sz_abstractfactory.destroy()


# -----------------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_abstractfactory", scope="function")
def szabstractfactory_fixture() -> SzAbstractFactory:
    """
    Single sz_abstractfactory object to use for all tests.
    """
    return SzAbstractFactoryMock()
