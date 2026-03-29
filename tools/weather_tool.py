"""
Weather Tool - Custom Tool 1

Fetches current weather for a city using the free wttr.in API.
No API key required!
"""

import requests
from base_tool import BaseTool


class WeatherTool(BaseTool):
    """Fetches current weather for a given city."""

    def execute(self, city: str, **kwargs) -> str:
        """Get weather for a city.
        
        Args:
            city (str): Name of the city (e.g., 'Riga', 'London')
            **kwargs: Additional arguments (ignored)
            
        Returns:
            str: Weather information or error message
        """
        try:
            response = requests.get(
                f"https://wttr.in/{city}?format=3",
                timeout=5
            )
            response.raise_for_status()
            return response.text
        except requests.exceptions.HTTPError:
            return f"Could not find weather for '{city}'. City may not exist."
        except Exception as e:
            return f"Weather fetch error: {e}"

    def get_declaration(self) -> dict:
        """Return function declaration for Gemini.
        
        Returns:
            dict: Function schema with name, description, and parameters
        """
        return {
            "name": "get_weather",
            "description": "Gets the current weather for a given city.",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "city": {
                        "type": "STRING",
                        "description": "Name of the city e.g. 'Riga', 'London'"
                    }
                },
                "required": ["city"]
            }
        }
