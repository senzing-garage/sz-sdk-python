#! /usr/bin/env python3

from senzing_truthset import TRUTHSET_DATASOURCES

from senzing import SzConfig, SzConfigManager, SzDiagnostic, SzEngine, SzError

INSTANCE_NAME = "Example1"
SETTINGS = {
    "PIPELINE": {
        "CONFIGPATH": "/etc/opt/senzing",
        "RESOURCEPATH": "/opt/senzing/g2/resources",
        "SUPPORTPATH": "/opt/senzing/data",
    },
    "SQL": {"CONNECTION": "sqlite3://na:na@/tmp/sqlite/G2C.db"},
}

try:
    sz_config = SzConfig(INSTANCE_NAME, SETTINGS)
    sz_configmanager = SzConfigManager(INSTANCE_NAME, SETTINGS)
    sz_diagnostic = SzDiagnostic(INSTANCE_NAME, SETTINGS)
    sz_engine = SzEngine(INSTANCE_NAME, SETTINGS)

    current_default_config_id = sz_configmanager.get_default_config_id()
    OLD_CONFIG_DEFINITION = sz_configmanager.get_config(current_default_config_id)
    config_handle = sz_config.import_config(OLD_CONFIG_DEFINITION)
    for data_source_code in TRUTHSET_DATASOURCES:
        sz_config.add_data_source(config_handle, data_source_code)
    NEW_CONFIG_DEFINITION = sz_config.export_config(config_handle)
    new_default_config_id = sz_configmanager.add_config(
        NEW_CONFIG_DEFINITION, "Add TruthSet datasources"
    )
    sz_configmanager.replace_default_config_id(
        current_default_config_id, new_default_config_id
    )
    sz_engine.reinitialize(new_default_config_id)
    sz_diagnostic.reinitialize(new_default_config_id)
except SzError as err:
    print(f"\nError: {err}\n")
