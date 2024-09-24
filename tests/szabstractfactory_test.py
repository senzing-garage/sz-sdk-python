#! /usr/bin/env python3

"""
TODO: szabstractfactory_test.py
"""

import pytest


from szconfig_test import SzConfigTest
from szconfigmanager_test import SzConfigManagerTest
from szdiagnostic_test import SzDiagnosticTest
from szengine_test import SzEngineTest
from szproduct_test import SzProductTest

from senzing_abstract import (
    SzAbstractFactoryAbstract,
    SzConfigAbstract,
    SzConfigManagerAbstract,
    SzDiagnosticAbstract,
    SzEngineAbstract,
    SzProductAbstract,
)

# -----------------------------------------------------------------------------
# SzAbstractFactory testcases
# -----------------------------------------------------------------------------


def test_create_sz_config(szabstractfactory: SzAbstractFactoryAbstract) -> None:
    """Test SzConfig().add_data_source()."""
    actual = szabstractfactory.create_sz_config()
    assert isinstance(actual, SzConfigAbstract)


def test_create_sz_configmanager(szabstractfactory: SzAbstractFactoryAbstract) -> None:
    """Test SzConfig().add_data_source()."""
    actual = szabstractfactory.create_sz_configmanager()
    assert isinstance(actual, SzConfigManagerAbstract)


def test_create_sz_diagnostic(szabstractfactory: SzAbstractFactoryAbstract) -> None:
    """Test SzConfig().add_data_source()."""
    actual = szabstractfactory.create_sz_diagnostic()
    assert isinstance(actual, SzDiagnosticAbstract)


def test_create_sz_engine(szabstractfactory: SzAbstractFactoryAbstract) -> None:
    """Test SzConfig().add_data_source()."""
    actual = szabstractfactory.create_sz_engine()
    assert isinstance(actual, SzEngineAbstract)


def test_create_sz_product(szabstractfactory: SzAbstractFactoryAbstract) -> None:
    """Test SzConfig().add_data_source()."""
    actual = szabstractfactory.create_sz_product()
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

    def create_sz_config(self) -> SzConfigAbstract:
        return SzConfigTest()

    def create_sz_configmanager(self) -> SzConfigManagerAbstract:
        return SzConfigManagerTest()

    def create_sz_diagnostic(self) -> SzDiagnosticAbstract:
        return SzDiagnosticTest()

    def create_sz_engine(self) -> SzEngineAbstract:
        return SzEngineTest()

    def create_sz_product(self) -> SzProductAbstract:
        return SzProductTest()
