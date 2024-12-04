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


def test_new_szexception(sz_product: SzProductAbstract) -> None:
    """Test SzProduct().get_license()."""
    _ = sz_product


# -----------------------------------------------------------------------------
# SzError fixtures
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
