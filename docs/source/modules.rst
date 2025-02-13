senzing
=======

The `senzing` Python package has 5 major modules / classes.
Senzing objects are created using an `Abstract Factory Pattern`_.

.. list-table:: Senzing classes
   :widths: 20 20 60
   :header-rows: 1

   * - Module
     - Class
     - Creation
   * - szconfig
     - SzConfig
     - `sz_config = sz_abstract_factory.create_config()`
   * - szconfigmanager
     - SzConfigManager
     - `sz_configmanager = sz_abstract_factory.create_configmanager()`
   * - szdiagnostic
     - SzDiagnostic
     - `sz_diagnostic = sz_abstract_factory.create_diagnostic()`
   * - szengine
     - SzEngine
     - `sz_engine = sz_abstract_factory.create_engine()`
   * - szproduct
     - SzProduct
     - `sz_product = sz_abstract_factory.create_product()`

.. toctree::
   :maxdepth: 4

   senzing

.. _Abstract Factory Pattern: https://en.wikipedia.org/wiki/Abstract_factory_pattern