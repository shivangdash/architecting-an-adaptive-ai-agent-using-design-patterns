"""
Tool Registry - Factory/Registry Pattern

Registers and dispatches tools dynamically without if-else chains.
This implements the Factory Pattern and satisfies Open/Closed Principle.
"""

from base_tool import BaseTool


class ToolRegistry:
    """Manages tool registration and execution.
    
    Implements the Factory Pattern to:
    - Register tools dynamically
    - Execute tools by name without tight coupling
    - Provide tool declarations to the Gemini model
    """

    def __init__(self):
        """Initialize empty tool dictionary."""
        self._tools: dict[str, BaseTool] = {}

    def register(self, name: str, tool: BaseTool) -> None:
        """Register a new tool.
        
        Args:
            name (str): Unique identifier for the tool
            tool (BaseTool): Instance of a tool that inherits from BaseTool
        """
        self._tools[name] = tool

    def execute(self, name: str, **kwargs):
        """Execute a registered tool by name.
        
        Args:
            name (str): Name of the tool to execute
            **kwargs: Arguments to pass to the tool
            
        Returns:
            Result from the tool's execute() method
            
        Raises:
            ValueError: If tool name not found in registry
        """
        if name not in self._tools:
            raise ValueError(f"Unknown tool: {name}")
        return self._tools[name].execute(**kwargs)

    def get_declarations(self) -> list[dict]:
        """Get function declarations for all registered tools.
        
        Returns:
            list[dict]: List of function declarations for Gemini function calling
        """
        return [tool.get_declaration() for tool in self._tools.values()]
