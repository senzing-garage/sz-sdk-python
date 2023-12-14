#! /usr/bin/env python3

"""
TODO: g2product_test.py
"""

# pylint: disable=E1101

from typing import Any, Dict, Union

import pytest

from senzing_abstract import g2product_abstract

# -----------------------------------------------------------------------------
# G2Config fixtures
# -----------------------------------------------------------------------------


@pytest.fixture(name="g2_product", scope="module")  # type: ignore[misc]
def g2product_fixture() -> g2product_abstract.G2ProductAbstract:
    """
    Object under test.
    """

    return G2ProductTest()


# -----------------------------------------------------------------------------
# G2ProductTest class
# -----------------------------------------------------------------------------


class G2ProductTest(g2product_abstract.G2ProductAbstract):
    """
    G2 product module access library.
    """

    # -------------------------------------------------------------------------
    # G2Product methods
    # -------------------------------------------------------------------------

    def destroy(self, *args: Any, **kwargs: Any) -> None:
        """None"""

    def init(
        self,
        module_name: str,
        ini_params: Union[str, Dict[Any, Any]],
        verbose_logging: int = 0,
        **kwargs: Any,
    ) -> None:
        """None"""

    def license(self, *args: Any, **kwargs: Any) -> str:
        return ""

    def version(self, *args: Any, **kwargs: Any) -> str:
        return ""


# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_destroy(g2_product: g2product_abstract.G2ProductAbstract) -> None:
    """Test G2Product().destroy()."""
    g2_product.destroy()


def test_init(g2_product: g2product_abstract.G2ProductAbstract) -> None:
    """Test G2Product().init()."""
    g2_product.init("", "")


def test_license(g2_product: g2product_abstract.G2ProductAbstract) -> None:
    """Test G2Product().license()."""
    g2_product.license()


def test_version(g2_product: g2product_abstract.G2ProductAbstract) -> None:
    """Test G2Product().version()."""
    g2_product.version()
