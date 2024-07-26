#! /usr/bin/env python3

"""
TODO: szengineflags_test.py
"""

from senzing_abstract import SzEngineFlags

# -----------------------------------------------------------------------------
# Test cases
# -----------------------------------------------------------------------------


def test_combine_flags() -> None:
    """Test SzProduct().get_license()."""
    x = SzEngineFlags.combine_flags(
        [
            SzEngineFlags.SZ_ENTITY_BRIEF_DEFAULT_FLAGS,
            SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS,
        ]
    )
    print(x)


def test_get_flag_int() -> None:
    """Test SzProduct().get_version()."""
    x = SzEngineFlags.get_flag_int(SzEngineFlags.SZ_ENTITY_BRIEF_DEFAULT_FLAGS)
    print(x)
