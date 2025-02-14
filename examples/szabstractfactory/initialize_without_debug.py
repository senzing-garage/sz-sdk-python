from senzing_core import SzAbstractFactoryCore

from senzing import SzError

try:
    INSTANCE_NAME = "Example"
    settings = {
        "PIPELINE": {
            "CONFIGPATH": "/etc/opt/senzing",
            "RESOURCEPATH": "/opt/senzing/er/resources",
            "SUPPORTPATH": "/opt/senzing/data",
        },
        "SQL": {"CONNECTION": "sqlite3://na:na@/tmp/sqlite/G2C.db"},
    }
    VERBOSE_LOGGING = 0
    sz_abstract_factory = SzAbstractFactoryCore(INSTANCE_NAME, settings, verbose_logging=VERBOSE_LOGGING)
    # Create an engine to show debug output
    sz_abstract_factory.create_engine()
except SzError as err:
    print(f"\nERROR: {err}\n")
