#! /usr/bin/env python3

"""
szconfigmanager.py is the abstract class for all implementations of SzConfigManager.
"""

# TODO: Determine specific SzErrors, Errors for "Raises:" documentation.

from abc import ABC, abstractmethod

from .szconfig import SzConfig
from .szhelpers import construct_help

# Metadata

__all__ = ["SzConfigManager"]
__version__ = "0.0.1"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = "2023-10-30"
__updated__ = "2023-11-08"

# -----------------------------------------------------------------------------
# SzConfigManager
# -----------------------------------------------------------------------------


class SzConfigManager(ABC):
    """
    SzConfigManager is the definition of the Senzing Python SDK that is
    implemented by packages such as szconfigmanager.py.
    """

    # -------------------------------------------------------------------------
    # Interface definition
    # -------------------------------------------------------------------------

    @abstractmethod
    def create_config_from_config_id(self, config_id: int) -> SzConfig:
        """
        The `create_config_from_config_id` method creates an in-memory Senzing configuration
        from a specific Senzing configuration stored in the Senzing database.

        Args:
            config_id (int): The configuration identifier of the desired Senzing configuration to retrieve.

        Returns:
            SzConfig: Represents an in-memory Senzing configuration that can be modified.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Example:

            .. literalinclude:: ../../examples/szconfigmanager/create_config_from_config_id.py
                :linenos:
                :language: python

            **Output:**

            .. literalinclude:: ../../examples/szconfigmanager/create_config_from_config_id.txt
                :linenos:
                :language: json
        """

    @abstractmethod
    def create_config_from_string(self, config_definition: str) -> SzConfig:
        """
        The `create_config_from_string` method creates an in-memory Senzing configuration
        from the given Senzing configuration JSON document.

        Args:
            config_definition (str): The Senzing configuration JSON document.

        Returns:
            SzConfig: Represents an in-memory Senzing configuration that can be modified.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Example:

            .. literalinclude:: ../../examples/szconfigmanager/create_config_from_string.py
                :linenos:
                :language: python

            **Output:**

            .. literalinclude:: ../../examples/szconfigmanager/create_config_from_string.txt
                :linenos:
                :language: json
        """

    @abstractmethod
    def create_config_from_template(self) -> SzConfig:
        """
        The `create_config_from_template` method creates an in-memory Senzing configuration
        from the template Senzing configuration JSON document located at PIPELINE.RESOURCEPATH/templates/g2config.json

        Args:
            config_definition (str): The Senzing configuration JSON document.

        Returns:
            SzConfig: Represents an in-memory Senzing configuration that can be modified.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Example:

            .. literalinclude:: ../../examples/szconfigmanager/create_config_from_template.py
                :linenos:
                :language: python

            **Output:**

            .. literalinclude:: ../../examples/szconfigmanager/create_config_from_template.txt
                :linenos:
                :language: json
        """

    @abstractmethod
    def get_configs(self) -> str:
        """
        The `get_configs` method retrieves a list of Senzing configurations from the Senzing database.

        Returns:
            str: A JSON document containing Senzing configurations.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Example:

            .. literalinclude:: ../../examples/szconfigmanager/get_configs.py
                :linenos:
                :language: python

            **Output:**

            .. literalinclude:: ../../examples/szconfigmanager/get_configs.txt
                :linenos:
                :language: json
        """

    @abstractmethod
    def get_default_config_id(self) -> int:
        """
        The `get_default_config_id` method retrieves from the Senzing database the configuration identifier of the default Senzing configuration.

        Returns:
            int:  A configuration identifier which identifies the current configuration in use.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Example:

            .. literalinclude:: ../../examples/szconfigmanager/get_default_config_id.py
                :linenos:
                :language: python

            **Output:**

            .. literalinclude:: ../../examples/szconfigmanager/get_default_config_id.txt
                :linenos:
                :language: json
        """

    @abstractmethod
    def register_config(self, config_definition: str, config_comment: str) -> int:
        """
        The `register_config` method adds a Senzing configuration JSON document to the Senzing database.

        Args:
            config_definition (str): The Senzing configuration JSON document.
            config_comment (str):  free-form string of comments describing the configuration document.

        Returns:
            int: A configuration identifier.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Example:

            .. literalinclude:: ../../examples/szconfigmanager/register_config.py
                :linenos:
                :language: python

            **Output:**

            .. literalinclude:: ../../examples/szconfigmanager/register_config.txt
                :linenos:
                :language: json
        """

    @abstractmethod
    def replace_default_config_id(self, current_default_config_id: int, new_default_config_id: int) -> None:
        """
        The `replace_default_config_id` method replaces the old configuration identifier with a new configuration identifier in the Senzing database.
        It is like a "compare-and-swap" instruction to serialize concurrent editing of configuration.
        If `current_default_config_id` is no longer the "current configuration identifier", the operation will fail.
        To simply set the default configuration ID, use `set_default_config_id`.

        Args:
            current_default_config_id (int): The configuration identifier to replace.
            new_default_config_id (int): The configuration identifier to use as the default.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Example:

            .. literalinclude:: ../../examples/szconfigmanager/replace_default_config_id.py
                :linenos:
                :language: python
        """

    @abstractmethod
    def set_default_config(self, config_definition: str, config_comment: str) -> int:
        """
        The `set_default_config` method replaces the current default Senzing configuration in the Senzing database.
        To serialize modifying of the configuration identifier, see `replace_default_config_id`.

        Args:
            config_definition (str): The Senzing configuration JSON document.
            config_comment (str):  free-form string of comments describing the configuration document.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Example:

            .. literalinclude:: ../../examples/szconfigmanager/set_default_config.py
                :linenos:
                :language: python

            **Output:**

            .. literalinclude:: ../../examples/szconfigmanager/set_default_config.txt
                :linenos:
                :language: json
        """

    @abstractmethod
    def set_default_config_id(self, config_id: int) -> None:
        """
        The `set_default_config_id` method replaces and sets a new configuration identifier in the Senzing database.
        To serialize modifying of the configuration identifier, see `replace_default_config_id`.

        Args:
            config_id (int): The configuration identifier of the Senzing Engine configuration to use as the default.

        Raises:
            TypeError: Incorrect datatype of input parameter.

        .. collapse:: Example:

            .. literalinclude:: ../../examples/szconfigmanager/set_default_config_id.py
                :linenos:
                :language: python
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
