#! /usr/bin/env python3

"""
TODO: szengineflags_test.py
"""

import json

from pytest_schema import schema

from senzing import SzEngineFlags

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_flags_by_name() -> None:
    """Test szengineflags.flags_by_name()."""
    actual = SzEngineFlags.flags_by_name()
    actual_as_dict = json.loads(actual)
    assert schema(test_flags_by_name_schema) == actual_as_dict


def test_flags_by_value() -> None:
    """Test szengineflags.flags_by_value()."""
    actual = SzEngineFlags.flags_by_value()
    actual_as_dict = json.loads(actual)
    assert schema(test_flags_by_value_schema) == actual_as_dict


# -----------------------------------------------------------------------------
# Schemas
# -----------------------------------------------------------------------------

test_flags_by_name_schema = {str, int}
test_flags_by_value_schema = {str, int}
