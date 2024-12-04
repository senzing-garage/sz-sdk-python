#! /usr/bin/env python3

"""
TODO: szproduct_test.py
"""


import pytest

from senzing import SzProduct

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_new_szexception(sz_product: SzProduct) -> None:
    """Test SzProduct().get_license()."""
    _ = sz_product


# -----------------------------------------------------------------------------
# SzError fixtures
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
