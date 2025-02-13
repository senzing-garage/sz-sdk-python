from senzing_core import SzAbstractFactoryCore

from senzing import SzError

try:
    # The value of config_id is made up.  Any object created by this AbstractFactory will fail.
    CONFIG_ID = 2787481550
    INSTANCE_NAME = "Example"
    settings = {
        "PIPELINE": {
            "CONFIGPATH": "/etc/opt/senzing",
            "RESOURCEPATH": "/opt/senzing/er/resources",
            "SUPPORTPATH": "/opt/senzing/data",
        },
        "SQL": {"CONNECTION": "sqlite3://na:na@/tmp/sqlite/G2C.db"},
    }
    sz_abstract_factory = SzAbstractFactoryCore(INSTANCE_NAME, settings, CONFIG_ID)
except SzError as err:
    print(f"\nERROR: {err}\n")
