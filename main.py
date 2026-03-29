"""
Main CLI Entry Point

Initializes the agent with all tools and runs an interactive CLI.
"""

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

from tool_registry import ToolRegistry
from memory_manager import MemoryManager
from agent import Agent
from tools.calculator_tool import CalculatorTool
from tools.time_tool import TimeTool
from tools.weather_tool import WeatherTool
from tools.translator_tool import TranslatorTool


def main():
    """Main entry point - Initialize agent and start CLI loop."""
    
    # Initialize tool registry and register all tools
    registry = ToolRegistry()
    registry.register("calculator", CalculatorTool())
    registry.register("get_time", TimeTool())
    registry.register("get_weather", WeatherTool())
    registry.register("translate_text", TranslatorTool())

    # Initialize memory manager
    memory = MemoryManager()
    
    # Initialize agent
    agent = Agent(registry, memory)

    # Print welcome message
    print("=" * 50)
    print("🤖 AI Personal Assistant")
    print("=" * 50)
    print("Type 'exit' to quit.\n")

    # Main CLI loop
    while True:
        try:
            user_input = input("You: ").strip()
            
            # Skip empty input
            if not user_input:
                continue
            
            # Check for exit command
            if user_input.lower() == "exit":
                print("Goodbye! 👋")
                break
            
            # Get response from agent
            response = agent.run(user_input)
            print(f"Agent: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
