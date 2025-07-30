.. sz-sdk-python documentation master file, created by
   sphinx-quickstart on Thu Dec 14 15:35:47 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

`senzing` Python package documentation
======================================

The `senzing`_ Python package contains the interface definitions
for the `senzing-core`_ and `senzing-grpc`_ implementation packages.

By using interface definitions, implementation-agnostic code can be written.
For example, the following code does not need to know the underlying implementation
of the Senzing Abstract Factory:

.. literalinclude:: ../../examples/docs/using_abstract_factory.py
      :linenos:
      :language: python

Similarly, interface definitions for Senzing objects can be used.
Example:

.. literalinclude:: ../../examples/docs/using_sz_engine.py
      :linenos:
      :language: python

The `senzing` Python package also includes constants and errors used across different Senzing Python
implementation classes.

As an abstract class, the `senzing` Python package is not used to create instances of
Senzing Abstract Factory, Senzing engine, etc.
Concrete classes, such as `senzing-core`_, are used in the creation of objects.
Example:

.. literalinclude:: ../../examples/docs/using_abstract_factory_core.py
      :linenos:
      :language: python



Senzing has additional Software Development Kits (SDKs)
for Java, Go, and C#.
Information for these SDKs can be found at `docs.senzing.com`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   senzing

References
==========

#. :ref:`genindex`
#. :ref:`modindex`
#. :ref:`search`
#. `GitHub`_
#. `Pypi`_
#. `senzing-core`_
#. `senzing-grpc`_

.. _docs.senzing.com: https://www.senzing.com/docs
.. _GitHub: https://github.com/senzing-garage/sz-sdk-python/tree/main/examples
.. _Pypi: https://pypi.org/project/senzing/
.. _senzing-core: https://garage.senzing.com/sz-sdk-python-core
.. _senzing-grpc: https://garage.senzing.com/sz-sdk-python-grpc
.. _senzing: https://github.com/senzing-garage/sz-sdk-python
