"""
Time Tool - Built-in Tool 2

Returns the current date and time.
"""

from datetime import datetime
from base_tool import BaseTool


class TimeTool(BaseTool):
    """Returns the current date and time."""

    def execute(self, **kwargs) -> str:
        """Get current date and time.
        
        Args:
            **kwargs: Additional arguments (ignored)
            
        Returns:
            str: Current date and time formatted string
        """
        return datetime.now().strftime("Current date and time: %Y-%m-%d %H:%M:%S")

    def get_declaration(self) -> dict:
        """Return function declaration for Gemini.
        
        Returns:
            dict: Function schema with name, description, and parameters
        """
        return {
            "name": "get_time",
            "description": "Returns the current date and time.",
            "parameters": {
                "type": "OBJECT",
                "properties": {}
            }
        }
