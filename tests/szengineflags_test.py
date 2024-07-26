#! /usr/bin/env python3

"""
TODO: szengineflags_test.py
"""

import pytest

from senzing_abstract import SzEngineFlags, SzError

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_combine_flags() -> None:
    """Test SzProduct().get_license()."""
    SzEngineFlags.combine_flags(
        [
            SzEngineFlags.SZ_ENTITY_BRIEF_DEFAULT_FLAGS,
            SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS,
        ]
    )


def test_combine_flags_using_strings() -> None:
    """Test SzProduct().get_license()."""
    SzEngineFlags.combine_flags(
        [
            "SZ_ENTITY_BRIEF_DEFAULT_FLAGS",
            "SZ_FIND_NETWORK_DEFAULT_FLAGS",
        ]
    )


def test_combine_flags_bad_string() -> None:
    """Test SzProduct().get_license()."""
    with pytest.raises(SzError):
        SzEngineFlags.combine_flags(
            [
                "BAD_STRING",
            ]
        )


def test_get_flag_int() -> None:
    """Test SzProduct().get_version()."""
    SzEngineFlags.get_flag_int(SzEngineFlags.SZ_ENTITY_BRIEF_DEFAULT_FLAGS)


def test_get_flag_int_using_strings() -> None:
    """Test SzProduct().get_version()."""
    SzEngineFlags.get_flag_int("SZ_ENTITY_BRIEF_DEFAULT_FLAGS")


def test_get_flag_int_bad_string() -> None:
    """Test SzProduct().get_version()."""
    with pytest.raises(SzError):
        SzEngineFlags.get_flag_int("BAD_STRING")
