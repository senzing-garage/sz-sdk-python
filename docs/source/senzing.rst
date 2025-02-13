senzing package
===============

In the examples, the creation of the Senzing objects has been abstracted to

.. literalinclude:: ../../examples/docs/import_sz_abstract_factory.py
      :linenos:
      :language: python

and

.. literalinclude:: ../../examples/docs/import_sz_engine.py
      :linenos:
      :language: python

Using the `senzing-core` Python package, the implementation looks like the following:


.. literalinclude:: ../../examples/helpers/setup_senzing.py
      :linenos:
      :language: python

Naturally, the `__init__.py` file needs to be modified to support importing the variables.
For the full implementation of the documentation examples, visit the source code on
`GitHub`_.

Submodules
----------

senzing.szabstractfactory module
--------------------------------

.. automodule:: senzing.szabstractfactory
   :members:
   :undoc-members:
   :show-inheritance:

senzing.szconfig module
-----------------------

.. automodule:: senzing.szconfig
   :members:
   :undoc-members:
   :show-inheritance:

senzing.szconfigmanager module
------------------------------

.. automodule:: senzing.szconfigmanager
   :members:
   :undoc-members:
   :show-inheritance:

senzing.szdiagnostic module
---------------------------

.. automodule:: senzing.szdiagnostic
   :members:
   :undoc-members:
   :show-inheritance:

senzing.szengine module
-----------------------

.. automodule:: senzing.szengine
   :members:
   :undoc-members:
   :show-inheritance:

senzing.szengineflags module
----------------------------

.. automodule:: senzing.szengineflags
   :members:
   :undoc-members:
   :show-inheritance:

senzing.szproduct module
------------------------

.. automodule:: senzing.szproduct
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: senzing
   :members:
   :undoc-members:
   :show-inheritance:


.. _GitHub: https://github.com/senzing-garage/sz-sdk-python/tree/main/examples