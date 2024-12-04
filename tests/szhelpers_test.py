#! /usr/bin/env python3

"""
TODO: szproduct_test.py
"""

from typing import Any

import pytest

from senzing import SzProductAbstract

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_construct_help_1(sz_product: SzProductAbstract) -> None:
    """Test SzProduct().get_license()."""
    sz_product.help()


def test_construct_help_2(sz_product: SzProductAbstract) -> None:
    """Test SzProduct().get_license()."""
    sz_product.help("get_version")


# -----------------------------------------------------------------------------
# SzConfig fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_product", scope="module")
def szproduct_fixture() -> SzProductAbstract:
    """
    Object under test.
    """

    return SzProductTest()


# -----------------------------------------------------------------------------
# SzProductTest class
# -----------------------------------------------------------------------------


class SzProductTest(SzProductAbstract):
    """
    SzProduct module access library.
    """

    # -------------------------------------------------------------------------
    # SzProduct methods
    # -------------------------------------------------------------------------

    def get_license(self, **kwargs: Any) -> str:
        return ""

    def get_version(self, **kwargs: Any) -> str:
        return ""
