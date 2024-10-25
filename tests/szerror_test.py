#! /usr/bin/env python3

"""
TODO: szproduct_test.py
"""

from typing import Any, Dict, Optional, Union

import pytest

from senzing_abstract import SzProductAbstract

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_new_szexception(sz_product: SzProductAbstract) -> None:
    """Test SzProduct().get_license()."""
    pass


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

    def destroy(self, *args: Any, **kwargs: Any) -> None:
        """None"""

    def initialize(
        self,
        instance_name: str,
        settings: Union[str, Dict[Any, Any]],
        verbose_logging: Optional[int] = 0,
        **kwargs: Any,
    ) -> None:
        """None"""

    def get_license(self, **kwargs: Any) -> str:
        return ""

    def get_version(self, **kwargs: Any) -> str:
        return ""
