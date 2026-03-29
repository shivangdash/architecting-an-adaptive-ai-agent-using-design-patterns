"""
Translator Tool - Custom Tool 2

Translates English text to other languages using the free MyMemory API.
No API key required!
"""

import requests
from base_tool import BaseTool


class TranslatorTool(BaseTool):
    """Translates English text to another language."""

    def execute(self, text: str, target_lang: str, **kwargs) -> str:
        """Translate text to a target language.
        
        Args:
            text (str): English text to translate
            target_lang (str): Target language code (e.g., 'lv', 'fr', 'de')
            **kwargs: Additional arguments (ignored)
            
        Returns:
            str: Translated text or error message
        """
        try:
            response = requests.get(
                "https://api.mymemory.translated.net/get",
                params={
                    "q": text,
                    "langpair": f"en|{target_lang}"
                },
                timeout=5
            )
            response.raise_for_status()
            return response.json()["responseData"]["translatedText"]
        except Exception as e:
            return f"Translation error: {e}"

    def get_declaration(self) -> dict:
        """Return function declaration for Gemini.
        
        Returns:
            dict: Function schema with name, description, and parameters
        """
        return {
            "name": "translate_text",
            "description": "Translates English text to another language using a language code.",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "text": {
                        "type": "STRING",
                        "description": "The English text to translate"
                    },
                    "target_lang": {
                        "type": "STRING",
                        "description": "Target language code: 'lv' Latvian, 'fr' French, 'de' German, 'es' Spanish, 'ja' Japanese, 'ru' Russian, 'it' Italian"
                    }
                },
                "required": ["text", "target_lang"]
            }
        }
