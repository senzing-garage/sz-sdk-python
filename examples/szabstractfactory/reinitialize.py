from senzing import SzError

from . import sz_abstract_factory

try:
    # Using get_active_config_id for demonstrations purposes.
    sz_engine = sz_abstract_factory.create_engine()
    CONFIG_ID = sz_engine.get_active_config_id()
    sz_abstract_factory.reinitialize(CONFIG_ID)
except SzError as err:
    print(f"\nERROR: {err}\n")
