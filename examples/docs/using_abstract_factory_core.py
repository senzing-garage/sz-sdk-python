import json

from senzing_core import SzAbstractFactoryCore

from senzing import SzAbstractFactory, SzEngineFlags, SzError


def perform_senzing_search(sz_abstract_factory: SzAbstractFactory, attributes: str) -> str:
    """Example Senzing search."""
    sz_engine = sz_abstract_factory.create_engine()
    flags = SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS
    search_profile = ""
    return sz_engine.search_by_attributes(attributes, flags, search_profile)


instance_name = "Example"
settings = {
    "PIPELINE": {
        "CONFIGPATH": "/etc/opt/senzing",
        "RESOURCEPATH": "/opt/senzing/er/resources",
        "SUPPORTPATH": "/opt/senzing/data",
    },
    "SQL": {"CONNECTION": "sqlite3://na:na@/tmp/sqlite/G2C.db"},
}

try:
    sz_abstract_factory = SzAbstractFactoryCore(instance_name, settings)
    attributes = json.dumps({"NAME_FULL": "Bob Smith", "EMAIL_ADDRESS": "bsmith@work.com"})
    search_results = perform_senzing_search(sz_abstract_factory, attributes)
    print(search_results)
except SzError as err:
    print(f"\nERROR: {err}\n")
