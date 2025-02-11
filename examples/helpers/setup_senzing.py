#! /usr/bin/env python3

from senzing_core import SzAbstractFactoryCore

from senzing import SzAbstractFactory

INSTANCE_NAME = "Example"
SETTINGS = {
    "PIPELINE": {
        "CONFIGPATH": "/etc/opt/senzing",
        "RESOURCEPATH": "/opt/senzing/er/resources",
        "SUPPORTPATH": "/opt/senzing/data",
    },
    "SQL": {"CONNECTION": "sqlite3://na:na@/tmp/sqlite/G2C.db"},
}


def get_sz_abstract_factory() -> SzAbstractFactory:
    """Example AbstractFactory"""
    return SzAbstractFactoryCore(INSTANCE_NAME, SETTINGS)
