"""
Base Tool Interface - Strategy Pattern

This abstract base class defines the contract that all tools must implement.
Every tool inherits from BaseTool and implements execute() and get_declaration().
"""

from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """Abstract base class for all tools.
    
    This enforces the Strategy Pattern, ensuring every tool has:
    - execute(): Performs the tool's logic
    - get_declaration(): Returns JSON schema for Gemini function calling
    """

    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """Execute the tool logic.
        
        Args:
            **kwargs: Tool-specific parameters
            
        Returns:
            Result of the tool execution
        """
        pass

    @abstractmethod
    def get_declaration(self) -> dict:
        """Return the Gemini function calling JSON schema.
        
        Returns:
            dict: Function declaration with name, description, and parameters
        """
        pass
