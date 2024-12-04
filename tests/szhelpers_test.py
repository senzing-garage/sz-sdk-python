#! /usr/bin/env python3

"""
TODO: szproduct_test.py
"""


import pytest

from senzing import SzProduct

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_construct_help_1(sz_product: SzProduct) -> None:
    """Test SzProduct().get_license()."""
    sz_product.help()


def test_construct_help_2(sz_product: SzProduct) -> None:
    """Test SzProduct().get_license()."""
    sz_product.help("get_version")


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
