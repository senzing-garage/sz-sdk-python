senzing package
===============

The `senzing`_ Python package has 5 major modules / classes.
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

In the examples, the creation of the Senzing Abstract Factory has been abstracted to

.. literalinclude:: ../../examples/docs/import_sz_abstract_factory.txt
      :language: python

and the creation of the Senzing objects has been abstracted to

.. literalinclude:: ../../examples/docs/import_sz_engine.txt
      :language: python

For the full implementation of the documentation examples, visit the source code on
`GitHub`_.

szabstractfactory
-----------------

.. automodule:: senzing.szabstractfactory
   :members:
   :undoc-members:
   :show-inheritance:

szconfig
--------

.. automodule:: senzing.szconfig
   :members:
   :undoc-members:
   :show-inheritance:

szconfigmanager
---------------

.. automodule:: senzing.szconfigmanager
   :members:
   :undoc-members:
   :show-inheritance:

szdiagnostic
------------

.. automodule:: senzing.szdiagnostic
   :members:
   :undoc-members:
   :show-inheritance:

szengine
--------

.. automodule:: senzing.szengine
   :members:
   :undoc-members:
   :show-inheritance:

szproduct
---------

.. automodule:: senzing.szproduct
   :members:
   :undoc-members:
   :show-inheritance:

szengineflags
-------------

.. automodule:: senzing.szengineflags
   :members:
   :undoc-members:
   :show-inheritance:

szerror
-------

.. automodule:: senzing.szerror
   :members:
   :undoc-members:
   :show-inheritance:

constants
---------

.. automodule:: senzing.constants
   :members:
   :undoc-members:
   :show-inheritance:

.. _Abstract Factory Pattern: https://en.wikipedia.org/wiki/Abstract_factory_pattern
.. _GitHub: https://github.com/senzing-garage/sz-sdk-python/tree/main/examples
.. _senzing-core: https://garage.senzing.com/sz-sdk-python-core
.. _senzing: https://github.com/senzing-garage/sz-sdk-python