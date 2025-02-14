from senzing import SzAbstractFactory, SzEngineFlags


def perform_senzing_search(sz_abstract_factory: SzAbstractFactory, attributes: str) -> str:
    """Example Senzing search."""
    sz_engine = sz_abstract_factory.create_engine()
    flags = SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS
    search_profile = ""
    return sz_engine.search_by_attributes(attributes, flags, search_profile)
