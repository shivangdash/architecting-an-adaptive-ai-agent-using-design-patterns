"""
Agent - ReAct Loop Implementation

Implements the Reason → Act → Observe loop using Google Gemini API.
The agent can use multiple tools and maintain conversation history.
"""

import os
from google import genai
from google.genai import types

from memory_manager import MemoryManager
from tool_registry import ToolRegistry


class Agent:
    """AI Agent implementing the ReAct (Reason-Act-Observe) pattern.
    
    This agent:
    - Uses Google Gemini for reasoning
    - Manages multiple tools through ToolRegistry
    - Maintains conversation history across turns
    - Implements function calling for tool execution
    """

    def __init__(self, registry: ToolRegistry, memory: MemoryManager):
        """Initialize the Agent.
        
        Args:
            registry (ToolRegistry): Tool registry containing all available tools
            memory (MemoryManager): Memory manager for conversation history
        """
        # Initialize Gemini client with API key
        self._client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        self._registry = registry
        self._memory = memory
        
        # Create tool declaration for Gemini function calling
        self._tool = types.Tool(
            function_declarations=registry.get_declarations()
        )
        
        # Create generate config with tools
        self._config = types.GenerateContentConfig(tools=[self._tool])

    def run(self, user_input: str) -> str:
        """Run a turn of the agent.
        
        Implements the ReAct loop:
        1. Reason: Model responds to user input
        2. Act: If model calls a tool, execute it
        3. Observe: Return results to model
        4. Repeat until model provides final answer
        
        Args:
            user_input (str): User's message
            
        Returns:
            str: Final response from the agent
        """
        # Create chat session with history
        chat = self._client.chats.create(
            model="gemini-2.5-flash",
            config=self._config,
            history=self._memory.get_history()
        )

        try:
            # Send user message to model (Reason)
            response = chat.send_message(user_input)

            # ReAct loop: Reason → Act → Observe
            while response.function_calls:
                # Collect all tool responses for this turn
                tool_response_parts = []

                # Execute each tool call (Act)
                for fc in response.function_calls:
                    try:
                        result = self._registry.execute(fc.name, **fc.args)
                    except Exception as e:
                        result = f"Tool error: {e}"

                    # Add tool response to parts list
                    tool_response_parts.append(
                        types.Part.from_function_response(
                            name=fc.name,
                            response={"result": str(result)}
                        )
                    )

                # Send observations back to model (Observe)
                response = chat.send_message(tool_response_parts)

            # Extract final text response
            final_text = response.text
            
            # Update memory with new history
            self._memory.set_history(chat.get_history())
            
            return final_text

        except Exception as e:
            return f"Agent error: {e}"
