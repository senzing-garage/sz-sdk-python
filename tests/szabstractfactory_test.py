#! /usr/bin/env python3

"""
TODO: szabstractfactory_test.py
"""

from typing import Any

import pytest

from senzing import (
    SzAbstractFactory,
    SzConfigManager,
    SzDiagnostic,
    SzEngine,
    SzProduct,
)

from . import SzConfigManagerTest, SzDiagnosticTest, SzEngineTest, SzProductTest

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
    return SzAbstractFactoryTest()


# -----------------------------------------------------------------------------
# SzDiagnosticTest class
# -----------------------------------------------------------------------------


class SzAbstractFactoryTest(SzAbstractFactory):
    """
    SzDiagnostic module access library.
    """

    # -------------------------------------------------------------------------
    # SzAbstractFactory methods
    # -------------------------------------------------------------------------

    def create_configmanager(self, **kwargs: Any) -> SzConfigManager:
        _ = kwargs
        return SzConfigManagerTest()

    def create_diagnostic(self, **kwargs: Any) -> SzDiagnostic:
        _ = kwargs
        return SzDiagnosticTest()

    def create_engine(self, **kwargs: Any) -> SzEngine:
        _ = kwargs
        return SzEngineTest()

    def create_product(self, **kwargs: Any) -> SzProduct:
        _ = kwargs
        return SzProductTest()

    def reinitialize(self, config_id: int, **kwargs: Any) -> None:
        _ = kwargs
