#! /usr/bin/env python3

from senzing_core import SzAbstractFactoryCore

from senzing import (
    SzAbstractFactory,
    SzConfig,
    SzConfigManager,
    SzDiagnostic,
    SzEngine,
    SzProduct,
)

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


def get_sz_config() -> SzConfig:
    """Example Config"""
    sz_abstract_factory = get_sz_abstract_factory()
    return sz_abstract_factory.create_config()


def get_sz_configmanager() -> SzConfigManager:
    """Example ConfigManager"""
    sz_abstract_factory = get_sz_abstract_factory()
    return sz_abstract_factory.create_configmanager()


def get_sz_diagnostic() -> SzDiagnostic:
    """Example Diagnostic"""
    sz_abstract_factory = get_sz_abstract_factory()
    return sz_abstract_factory.create_diagnostic()


def get_sz_engine() -> SzEngine:
    """Example Engine"""
    sz_abstract_factory = get_sz_abstract_factory()
    return sz_abstract_factory.create_engine()


def get_sz_product() -> SzProduct:
    """Example Product"""
    sz_abstract_factory = get_sz_abstract_factory()
    return sz_abstract_factory.create_product()
