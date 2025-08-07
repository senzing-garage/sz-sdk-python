"""
szproduct_test.py
"""

import pytest

from senzing import SzProduct
from senzing_mock import SzProductMock

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

    return SzProductMock()
