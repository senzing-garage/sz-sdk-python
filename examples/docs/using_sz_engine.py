from senzing import SzEngine, SzEngineFlags


def perform_senzing_search(sz_engine: SzEngine, attributes: str) -> str:
    """Example Senzing search."""
    flags = SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS
    search_profile = ""
    return sz_engine.search_by_attributes(attributes, flags, search_profile)
