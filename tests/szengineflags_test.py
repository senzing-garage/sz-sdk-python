#! /usr/bin/env python3

"""
TODO: szengineflags_test.py
"""

from pytest_schema import schema

from senzing import SzEngineFlags

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_flags_by_name() -> None:
    """Test szengineflags.flags_by_name()."""
    actual = SzEngineFlags.flags_by_name()
    assert schema(test_flags_by_name_schema) == actual


def test_flags_by_value() -> None:
    """Test szengineflags.flags_by_value()."""
    actual = SzEngineFlags.flags_by_value()
    assert schema(test_flags_by_value_schema) == actual


# -----------------------------------------------------------------------------
# Schemas
# -----------------------------------------------------------------------------

test_flags_by_name_schema = {str, int}
test_flags_by_value_schema = {int, str}
