#! /usr/bin/env python3

"""
szconfig.py is the abstract class for all implementations of szconfig.
"""

# TODO: Determine specific SzErrors, Errors for "Raises:" documentation.

from abc import ABC, abstractmethod

from .szhelpers import construct_help

# Metadata

__all__ = ["SzConfig"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2023-10-30"
__updated__ = "2023-11-08"

# -----------------------------------------------------------------------------
# SzConfig
# -----------------------------------------------------------------------------


class SzConfig(ABC):
    """
    SzConfig is the definition of the Senzing Python SDK that is
    implemented by packages such as szconfig.py.
    """

    # -------------------------------------------------------------------------
    # Interface definition
    # -------------------------------------------------------------------------

    @abstractmethod
    def add_data_source(self, config_handle: int, data_source_code: str) -> str:
        """
        The `add_data_source` method adds a data source to an existing in-memory configuration.

        Args:
            config_handle (int): An identifier of an in-memory configuration. Usually created by the `create` or `load` methods.
            data_source_code (str): Name of data source code to add.

        Returns:
            str: A string containing a JSON document listing the newly created data source.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Examples:

            .. collapse:: Core implementation:

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-core/refs/heads/main/examples/szconfig/add_data_source.py
                    :linenos:
                    :language: python

                **Output:**

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-core/refs/heads/main/examples/szconfig/add_data_source.txt
                    :linenos:
                    :language: json

            .. collapse:: gRPC implementation:

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/add_data_source.py
                    :linenos:
                    :language: python

                **Output:**

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/add_data_source.txt
                    :linenos:
                    :language: json
        """

    @abstractmethod
    def close_config(self, config_handle: int) -> None:
        """
        The `close_config` method cleans up the Senzing SzConfig object pointed to by the `config_handle`.

        Args:
            config_handle (int): An identifier of an in-memory configuration. Usually created by the `create_config` or `import_config` methods.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Examples:

            .. collapse:: Core implementation:

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-core/refs/heads/main/examples/szconfig/create_and_close.py
                    :linenos:
                    :language: python

                **Output:**

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-core/refs/heads/main/examples/szconfig/create_and_close.txt
                    :linenos:
                    :language: json

            .. collapse:: gRPC implementation:

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/create_and_close.py
                    :linenos:
                    :language: python

                **Output:**

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/create_and_close.txt
                    :linenos:
                    :language: json
        """

    @abstractmethod
    def create_config(self) -> int:
        """
        The `create_config` method creates an in-memory Senzing configuration
        from the `g2config.json` template configuration file located
        in the PIPELINE.RESOURCEPATH path.
        A handle is returned to identify the in-memory configuration.
        The handle is used by the `add_data_source`, `list_data_sources`,
        `delete_data_source`, and `export_config` methods.
        The handle is terminated by the `close_config` method.

        Returns:
            int: A pointer to an in-memory Senzing configuration.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Examples:

            .. collapse:: Core implementation:

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-core/refs/heads/main/examples/szconfig/create_and_close.py
                    :linenos:
                    :language: python

                **Output:**

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-core/refs/heads/main/examples/szconfig/create_and_close.txt
                    :linenos:
                    :language: json

            .. collapse:: gRPC implementation:

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/create_and_close.py
                    :linenos:
                    :language: python

                **Output:**

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/create_and_close.txt
                    :linenos:
                    :language: json
        """

    @abstractmethod
    def delete_data_source(self, config_handle: int, data_source_code: str) -> None:
        """
        The `delete_data_source` method removes a data source from an existing in-memory configuration.

        Args:
            config_handle (int): An identifier of an in-memory configuration. Usually created by the `create` or `load` methods.
            data_source_code (str): Name of data source code to delete.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Examples:

            .. collapse:: Core implementation:

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-core/refs/heads/main/examples/szconfig/delete_data_source.py
                    :linenos:
                    :language: python

                **Output:**

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-core/refs/heads/main/examples/szconfig/delete_data_source.txt
                    :linenos:
                    :language: json

            .. collapse:: gRPC implementation:

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/delete_data_source.py
                    :linenos:
                    :language: python

                **Output:**

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/delete_data_source.txt
                    :linenos:
                    :language: json
        """

    @abstractmethod
    def export_config(self, config_handle: int) -> str:
        """
        The `export_config` method creates a JSON string representation of the Senzing SzConfig object.

        Args:
            config_handle (int): An identifier of an in-memory configuration. Usually created by the `create` or `load` methods.

        Returns:
            str: A string containing a JSON Document representation of the Senzing SzConfig object.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Examples:

            .. collapse:: Core implementation:

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-core/refs/heads/main/examples/szconfig/export_config.py
                    :linenos:
                    :language: python

                **Output:**

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-core/refs/heads/main/examples/szconfig/export_config.txt
                    :linenos:
                    :language: json

            .. collapse:: gRPC implementation:

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/export_config.py
                    :linenos:
                    :language: python

                **Output:**

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/export_config.txt
                    :linenos:
                    :language: json
        """

    @abstractmethod
    def get_data_sources(self, config_handle: int) -> str:
        """
        The `get_data_sources` method returns a JSON document of data sources
        contained in an in-memory configuration.

        Args:
            config_handle (int): An identifier of an in-memory configuration. Usually created by the `create` or `load` methods.

        Returns:
            str: A string containing a JSON document listing all of the data sources.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Examples:

            .. collapse:: Core implementation:

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-core/refs/heads/main/examples/szconfig/get_data_sources.py
                    :linenos:
                    :language: python

                **Output:**

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-core/refs/heads/main/examples/szconfig/get_data_sources.txt
                    :linenos:
                    :language: json

            .. collapse:: gRPC implementation:

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/get_data_sources.py
                    :linenos:
                    :language: python

                **Output:**

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/get_data_sources.txt
                    :linenos:
                    :language: json
        """

    @abstractmethod
    def import_config(self, config_definition: str) -> int:
        """
        The `import_config` method initializes an in-memory Senzing SzConfig object from a JSON string.
        A handle is returned to identify the in-memory configuration.
        The handle is used by the `add_data_source`, `get_data_sources`,
        `delete_data_source`, and `save` methods.
        The handle is terminated by the `close` method.

        Args:
            config_definition (str): A JSON document containing the Senzing configuration.

        Returns:
            int: An identifier (config_handle) of an in-memory configuration.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Examples:

            .. collapse:: Core implementation:

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/import_config.py
                    :linenos:
                    :language: python

                **Output:**

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/import_config.txt
                    :linenos:
                    :language: json

            .. collapse:: gRPC implementation:

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/import_config.py
                    :linenos:
                    :language: python

                **Output:**

                .. rli:: https://raw.githubusercontent.com/senzing-garage/sz-sdk-python-grpc/refs/heads/main/examples/szconfig/import_config.txt
                    :linenos:
                    :language: json
        """

    # -------------------------------------------------------------------------
    # Convenience methods
    # -------------------------------------------------------------------------

    def help(self, method_name: str = "") -> str:
        """
        Return the help for a particular message.

        Args:
            method_name (str): The name of the method. (e.g. "init"). If empty, a list of methods and descriptions is returned.

        Returns:
            str: The Help information about the requested method
        """
        return construct_help(self, method_name=method_name)
