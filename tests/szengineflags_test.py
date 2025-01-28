#! /usr/bin/env python3

"""
TODO: szengineflags_test.py
"""


from senzing import SzEngineFlags

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_flags_by_name() -> None:
    """Test szengineflags.flags_by_name()."""
    actual = SzEngineFlags.flags_by_name()
    # assert schema(test_flags_by_name_schema) == actual
    assert isinstance(actual, dict)
    for k, v in actual.items():
        assert isinstance(k, str) and isinstance(v, int)


def test_flags_by_value() -> None:
    """Test szengineflags.flags_by_value()."""
    actual = SzEngineFlags.flags_by_value()
    # assert schema(test_flags_by_value_schema) == actual
    assert isinstance(actual, dict)
    for k, v in actual.items():
        assert isinstance(k, int) and isinstance(v, str)


# -----------------------------------------------------------------------------
# Schemas
# -----------------------------------------------------------------------------

test_flags_by_name_schema = {str, int}
test_flags_by_value_schema = {int, str}
