"""
Calculator Tool - Built-in Tool 1

Evaluates mathematical expressions safely using Python's eval
with restricted builtins for security.
"""

from base_tool import BaseTool


class CalculatorTool(BaseTool):
    """Evaluates mathematical expressions safely."""

    def execute(self, expression: str, **kwargs) -> str:
        """Execute a mathematical expression.
        
        Args:
            expression (str): Math expression to evaluate (e.g., '100 * 3 + 50')
            **kwargs: Additional arguments (ignored)
            
        Returns:
            str: Result of the calculation or error message
        """
        try:
            result = eval(expression, {"__builtins__": {}})
            return str(result)
        except Exception as e:
            return f"Calculation error: {e}"

    def get_declaration(self) -> dict:
        """Return function declaration for Gemini.
        
        Returns:
            dict: Function schema with name, description, and parameters
        """
        return {
            "name": "calculator",
            "description": "Evaluates a math expression like '2 + 2 * 5'.",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "expression": {
                        "type": "STRING",
                        "description": "A valid math expression e.g. '100 * 3 + 50'"
                    }
                },
                "required": ["expression"]
            }
        }
