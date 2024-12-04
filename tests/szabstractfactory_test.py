#! /usr/bin/env python3

"""
TODO: szabstractfactory_test.py
"""

from typing import Any

import pytest

from senzing import (
    SzAbstractFactoryAbstract,
    SzConfigAbstract,
    SzConfigManagerAbstract,
    SzDiagnosticAbstract,
    SzEngineAbstract,
    SzProductAbstract,
)
from szconfig_test import SzConfigTest
from szconfigmanager_test import SzConfigManagerTest
from szdiagnostic_test import SzDiagnosticTest
from szengine_test import SzEngineTest
from szproduct_test import SzProductTest

# -----------------------------------------------------------------------------
# SzAbstractFactory testcases
# -----------------------------------------------------------------------------


def test_create_config(szabstractfactory: SzAbstractFactoryAbstract) -> None:
    """Test SzConfig().add_data_source()."""
    actual = szabstractfactory.create_config()
    assert isinstance(actual, SzConfigAbstract)


def test_create_configmanager(szabstractfactory: SzAbstractFactoryAbstract) -> None:
    """Test SzConfig().add_data_source()."""
    actual = szabstractfactory.create_configmanager()
    assert isinstance(actual, SzConfigManagerAbstract)


def test_create_diagnostic(szabstractfactory: SzAbstractFactoryAbstract) -> None:
    """Test SzConfig().add_data_source()."""
    actual = szabstractfactory.create_diagnostic()
    assert isinstance(actual, SzDiagnosticAbstract)


def test_create_engine(szabstractfactory: SzAbstractFactoryAbstract) -> None:
    """Test SzConfig().add_data_source()."""
    actual = szabstractfactory.create_engine()
    assert isinstance(actual, SzEngineAbstract)


def test_create_product(szabstractfactory: SzAbstractFactoryAbstract) -> None:
    """Test SzConfig().add_data_source()."""
    actual = szabstractfactory.create_product()
    assert isinstance(actual, SzProductAbstract)


# -----------------------------------------------------------------------------
# SzAbstractFactory fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="szabstractfactory", scope="module")
def szabstractfactory_fixture() -> SzAbstractFactoryAbstract:
    """
    Single sz_abstractfactory object to use for all tests.
    """
    return SzAbstractFactoryTest()


# -----------------------------------------------------------------------------
# SzDiagnosticTest class
# -----------------------------------------------------------------------------


class SzAbstractFactoryTest(SzAbstractFactoryAbstract):
    """
    SzDiagnostic module access library.
    """

    # -------------------------------------------------------------------------
    # SzAbstractFactory methods
    # -------------------------------------------------------------------------

    def create_config(self, **kwargs: Any) -> SzConfigAbstract:
        _ = kwargs
        return SzConfigTest()

    def create_configmanager(self, **kwargs: Any) -> SzConfigManagerAbstract:
        _ = kwargs
        return SzConfigManagerTest()

    def create_diagnostic(self, **kwargs: Any) -> SzDiagnosticAbstract:
        _ = kwargs
        return SzDiagnosticTest()

    def create_engine(self, **kwargs: Any) -> SzEngineAbstract:
        _ = kwargs
        return SzEngineTest()

    def create_product(self, **kwargs: Any) -> SzProductAbstract:
        _ = kwargs
        return SzProductTest()

    def reinitialize(self, config_id: int, **kwargs: Any) -> None:
        _ = kwargs
