#! /usr/bin/env python3

"""
TODO: szproduct_test.py
"""


import pytest

from senzing import SzProduct

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


# def test_destroy(sz_product: SzProduct) -> None:
#     """Test SzProduct().destroy()."""
#     sz_product.destroy()


# def test_initialize(sz_product: SzProduct) -> None:
#     """Test SzProduct().initialize()."""
#     sz_product.initialize("", "")


def test_get_license(sz_product: SzProduct) -> None:
    """Test SzProduct().get_license()."""
    sz_product.get_license()


def test_get_version(sz_product: SzProduct) -> None:
    """Test SzProduct().get_version()."""
    sz_product.get_version()


# -----------------------------------------------------------------------------
# SzConfig fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_product", scope="module")
def szproduct_fixture() -> SzProduct:
    """
    Object under test.
    """

    return SzProductTest()


# -----------------------------------------------------------------------------
# SzProductTest class
# -----------------------------------------------------------------------------


class SzProductTest(SzProduct):
    """
    SzProduct module access library.
    """

    # -------------------------------------------------------------------------
    # SzProduct methods
    # -------------------------------------------------------------------------

    def get_license(self) -> str:
        return ""

    def get_version(self) -> str:
        return ""
