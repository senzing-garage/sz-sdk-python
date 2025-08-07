"""
szproduct_test.py
"""

import pytest

from senzing import SzProduct
from senzing_mock import SzProductMock

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_get_license(sz_product: SzProduct) -> None:
    """Test SzProduct.get_license()."""
    sz_product.get_license()


def test_get_version(sz_product: SzProduct) -> None:
    """Test SzProduct.get_version()."""
    sz_product.get_version()


def test_help_1(sz_product: SzProduct) -> None:
    """Test SzProduct.help()."""
    sz_product.help()


def test_help_2(sz_product: SzProduct) -> None:
    """Test SzProduct.help(...)."""
    sz_product.help("get_license")


# -----------------------------------------------------------------------------
# Unique testcases
# -----------------------------------------------------------------------------


# def test_initialize(sz_product: SzProduct) -> None:
#     """Test SzProduct.initialize()."""
#     sz_product.initialize("", "")


# def test_destroy(sz_product: SzProduct) -> None:
#     """Test SzProduct.destroy()."""
#     sz_product.destroy()


# -----------------------------------------------------------------------------
# Fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="sz_product", scope="module")
def szproduct_fixture() -> SzProduct:
    """
    Object under test.
    """

    return SzProductMock()
