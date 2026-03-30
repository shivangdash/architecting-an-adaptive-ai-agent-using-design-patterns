# Architecting an Adaptive AI Agent using Design Patterns

A production-ready AI agent framework that demonstrates best practices in architecting adaptive AI systems using proven design patterns. This project implements the **ReAct (Reason-Act-Observe)** loop pattern combined with classic software design patterns: **Factory**, **Registry**, **Strategy**, and **Single Responsibility**.

## 🎯 Overview

This project implements an intelligent personal assistant powered by Google Gemini that:
- **Reasons** about user requests using advanced language models
- **Executes tools dynamically** without hardcoding logic
- **Maintains conversation context** across multiple turns
- **Handles multi-step tasks** through agentic reasoning
- **Extends easily** by adding new tools without modifying core code

## 🏗️ Architecture & Design Patterns

### Core Design Patterns

| Pattern | Implementation | Benefit |
|---------|-----------------|---------|
| **ReAct Loop** | Agent reasoning cycle with Gemini | Transparent reasoning and multi-step problem solving |
| **Factory Pattern** | ToolRegistry creates and manages tools | Loose coupling, zero hardcoded if-else chains |
| **Registry Pattern** | ToolRegistry dynamic tool dispatch | Scalability and dynamic tool lookup |
| **Strategy Pattern** | BaseTool interface for tool implementations | Polymorphic tool execution with consistent interface |
| **Single Responsibility** | Separate Agent, Tools, Memory, Registry classes | High maintainability and testability |

### Key Architectural Principles

- **Open/Closed Principle**: Open for extension (new tools), closed for modification
- **Dependency Inversion**: Agent depends on abstractions (BaseTool), not concrete implementations
- **Composition over Inheritance**: Agent composes Registry and MemoryManager
- **Don't Repeat Yourself (DRY)**: Common tool behavior centralized in BaseTool

## 📋 Features

- ✅ **ReAct Loop Implementation**: Transparent Reason → Act → Observe → Repeat pattern
- ✅ **Multi-Tool Support**: Calculator, Time queries, Weather lookups, Text translation  
- ✅ **Function Calling**: Gemini automatically invokes appropriate tools
- ✅ **Conversation Memory**: Maintains full context across turns using memory manager
- ✅ **Extensible Architecture**: Add new tools with just a few lines of code
- ✅ **Google Gemini Integration**: Powers (gemini-2.5-flash) for state-of-the-art reasoning
- ✅ **Interactive CLI**: User-friendly command-line interface
- ✅ **Clean Code Patterns**: Factory, Registry, Strategy, and Single Responsibility

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key (Get it free at [Google AI Studio](https://aistudio.google.com/app/apikeys))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shivangdash/Architecting-an-Adaptive-AI-Agent-using-Design-Patterns.git
   cd Architecting-an-Adaptive-AI-Agent-using-Design-Patterns
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```
   
   Or manually create a `.env` file with:
   ```
   GEMINI_API_KEY=your_actual_gemini_api_key
   ```

### Usage

Start the interactive CLI:
```bash
python main.py
```

You'll see:
```
==================================================
🤖 AI Personal Assistant
==================================================
Type 'exit' to quit.

You: 
```

### Example Interactions

```
You: What's 25 + 17?
Agent: The sum of 25 and 17 is 42.

You: What time is it?
Agent: The current time is 3:45 PM.

You: Translate "Hello World" to Spanish
Agent: "Hello World" in Spanish is "Hola Mundo".

You: What's the weather in Tokyo?
Agent: The weather in Tokyo is...
```

## 📁 Project Structure

```
.
├── agent.py                 # ReAct loop + Gemini integration
├── base_tool.py             # Abstract base class (Strategy pattern)
├── tool_registry.py         # Factory/Registry pattern - tool management
├── memory_manager.py        # Conversation history storage
├── main.py                  # CLI entry point
├── requirements.txt         # Python dependencies
├── tools/                   # Tool implementations
│   ├── __init__.py
│   ├── calculator_tool.py   # Mathematical expression evaluator
│   ├── time_tool.py         # Current date/time provider
│   ├── weather_tool.py      # Weather info lookup
│   └── translator_tool.py   # Text translation service
├── .env                     # Environment variables (not in repo)
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

### Class Responsibilities

- **agent.py**: Implements ReAct loop, manages Gemini API calls, handles tool execution
- **base_tool.py**: Defines `BaseTool` abstract base class with `execute()` and `get_declaration()` methods
- **tool_registry.py**: Manages tool registration, lookup, and dispatch via `ToolRegistry` class
- **memory_manager.py**: Stores and retrieves conversation history via `MemoryManager` class
- **main.py**: Initializes components and runs interactive CLI loop
- **tools/***: Individual tool implementations, each inheriting from `BaseTool`

## 🛠️ Available Tools

### Calculator Tool (`calculator`)
Safely evaluates mathematical expressions using Python's `eval()` with restricted builtins.
- **Input**: Mathematical expression string (e.g., `"25 + 17"`, `"100 * 2.5"`)
- **Output**: Numeric result or error message
- **Example**: `"Calculate 100 * 2.5"` → `"250.0"`

### Time Tool (`get_time`)
Provides current date and time information.
- **Input**: None (or ignored if provided)
- **Output**: Current time as formatted string
- **Example**: `"What time is it?"` → `"3:45 PM"`

### Weather Tool (`get_weather`)
Fetches weather information for specified locations.
- **Input**: Location name (city/region)
- **Output**: Current weather conditions
- **Example**: `"What's the weather in Tokyo?"` → Weather details for Tokyo

### Translator Tool (`translate_text`)
Translates text between languages using external translation API.
- **Input**: Text and target language
- **Output**: Translated text
- **Example**: `"Translate hello to Spanish"` → `"Hola"`

## 🧠 How It Works

### The ReAct Loop Pattern

The agent implements a **Reason-Act-Observe** loop:

```
1. REASON
   User input → Gemini analyzes the request
   Model determines what action(s) to take

2. ACT  
   Model selects tool(s) to call via function calling
   Agent executes tool(s) via ToolRegistry
   
3. OBSERVE
   Tool results returned to model
   Model processes observations
   
4. LOOP or RESPOND
   If more steps needed → Go to REASON
   Else → Return final response to user
```

### Execution Flow

```
┌─────────────────┐
│   User Input    │
└────────┬────────┘
         ▼
    ┌─────────────────────────┐
    │ Agent.run()             │
    │ Create chat session     │
    └────────┬────────────────┘
             ▼
    ┌─────────────────────────┐
    │ Gemini: REASON          │
    │ Analyze user request    │
    └────────┬────────────────┘
             ▼
    ┌─────────────────────────┐
    │ Call functions?         │
    └────────┬────────────────┘
       No    │    Yes
         │   ▼
         │ ┌─────────────────────────┐
         │ │ Agent: ACT              │
         │ │ ToolRegistry.execute()  │
         │ │ Get tool results        │
         │ └────────┬────────────────┘
         │          ▼
         │ ┌─────────────────────────┐
         │ │ Gemini: OBSERVE         │
         │ │ Process tool results    │
         │ │ More calls needed?      │
         │ └────────┬────────────────┘
         │      Yes│   No
         │      │  └────┐
         │      └───────┤
         │              ▼
         │      ┌─────────────────────┐
         └─────►│ Return Response     │
              │ Update Memory      │
              └─────────────────────┘

## 🔧 Extending the Agent - Add a New Tool

Adding a new tool requires just **2 simple steps**:

### Step 1: Create Tool Class

Create a new file in `tools/` directory that inherits from `BaseTool`:

```python
# tools/currency_tool.py
from base_tool import BaseTool

class CurrencyTool(BaseTool):
    """Convert between currencies."""
    
    def execute(self, amount: float, from_currency: str, to_currency: str) -> str:
        """Execute currency conversion.
        
        Args:
            amount: Amount to convert
            from_currency: Source currency code (e.g., 'USD')
            to_currency: Target currency code (e.g., 'EUR')
            
        Returns:
            str: Conversion result
        """
        # Your conversion logic here
        # e.g., fetch rates from API, calculate result
        return f"{amount} {from_currency} = X {to_currency}"
    
    def get_declaration(self) -> dict:
        """Declare function for Gemini function calling."""
        return {
            "name": "convert_currency",
            "description": "Converts amount from one currency to another",
            "parameters": {
                "type": "OBJECT",
                "properties": {
                    "amount": {"type": "NUMBER", "description": "Amount to convert"},
                    "from_currency": {"type": "STRING", "description": "Source currency (USD, EUR, etc)"},
                    "to_currency": {"type": "STRING", "description": "Target currency"},
                },
                "required": ["amount", "from_currency", "to_currency"],
            }
        }
```

### Step 2: Register the Tool

In `main.py`, add one line to register your tool:

```python
from tools.currency_tool import CurrencyTool

# In main() function, after creating registry:
registry.register("convert_currency", CurrencyTool())
```

**That's it!** The agent now understands and can use currency conversion. No modifications to agent.py, tool_registry.py, or any other core files needed.

### Key Points for Tool Implementation

1. **Inherit from `BaseTool`**: Ensures consistent interface
2. **Implement `execute()`**: Contains tool logic, receives parameters as kwargs
3. **Implement `get_declaration()`**: Returns JSON schema for Gemini function calling
4. **Use meaningful names**: Tool name in registry should match function declaration name
5. **Handle errors gracefully**: Return error messages instead of raising exceptions

## 📦 Dependencies

The project uses minimal external dependencies:

- **google-genai** (v0.3.0+): Official Google Gemini API client for Python
- **python-dotenv** (v1.0.0+): Load environment variables from `.env` files
- **requests** (v2.31.0+): HTTP library for external API calls (used by weather/translator tools)

See [requirements.txt](requirements.txt) for exact versions. Install all with:
```bash
pip install -r requirements.txt
```

## 🔐 Environment Configuration

### Set Your API Key

1. Get a free Google Gemini API key at [aistudio.google.com](https://aistudio.google.com/app/apikeys)

2. Create a `.env` file in the project root:
   ```bash
   echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
   ```

3. Or manually create `.env` and add:
   ```
   GEMINI_API_KEY=sk-your_api_key_here
   ```

### Security Notes

- **Never commit `.env` to version control** - it contains sensitive credentials
- Add `.env` to `.gitignore` if not already present
- Keep your API key private and rotate if accidentally exposed
- The `load_dotenv()` call in `main.py` automatically loads variables from `.env`

## 💡 Design Principles & Patterns Applied

### SOLID Principles

- **S**ingle Responsibility: Each class has one reason to change
  - `Agent` handles reasoning/acting
  - `ToolRegistry` handles tool management
  - `MemoryManager` handles history
  - `BaseTool` defines tool interface

- **O**pen/Closed: Open for extension (add tools), closed for modification (core code)
  - New tools don't require changes to Agent or ToolRegistry

- **L**iskov Substitution: Any tool can replace another (all inherit BaseTool)

- **I**nterface Segregation: Minimal tool interface (execute + get_declaration)

- **D**ependency Inversion: Agent depends on abstractions, not concrete tools

### Design Patterns Used

1. **ReAct Pattern**: Reason-Act-Observe loop for multi-step problem solving
2. **Factory Pattern**: ToolRegistry creates and manages tool instances
3. **Registry Pattern**: Dynamic tool lookup without hardcoded if-else chains
4. **Strategy Pattern**: Different tool implementations with consistent interface
5. **Template Method**: BaseTool defines contract each tool must fulfill

## 🧪 Testing

### Manual Testing

Run the agent and try different queries:

```bash
python main.py
```

**Test Cases to Try:**

```
# Math operations
You: What's 100 * 25?
You: Calculate (50 + 30) / 4

# Time queries  
You: What time is it?
You: Tell me the current date and time

# Geography/Weather
You: What's the weather in New York?
You: Is it raining in London?

# Translation
You: Translate "Good morning" to French
You: How do you say "thank you" in German?

# Multi-step reasoning
You: It's currently 3 PM. If I wait 2 hours, what time will it be?
You: Convert 100 USD to Euros and tell me the current time

# Exit
You: exit
```

### Unit Testing

To add unit tests for individual tools:

```python
# tests/test_calculator_tool.py
import unittest
from tools.calculator_tool import CalculatorTool

class TestCalculatorTool(unittest.TestCase):
    def setUp(self):
        self.tool = CalculatorTool()
    
    def test_addition(self):
        result = self.tool.execute(expression="2 + 2")
        self.assertEqual(result, "4")
    
    def test_complex_expression(self):
        result = self.tool.execute(expression="(10 + 5) * 2")
        self.assertEqual(result, "30")

if __name__ == "__main__":
    unittest.main()
```

## 🤝 Contributing

Contributions are welcome! Here's how to contribute:

### For Bug Reports or Issues
1. Open an issue with clear description
2. Include steps to reproduce
3. Share error messages or logs

### For New Tools or Features

1. **Fork the repository** and create a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Implement your tool** following the [Extending the Agent](#-extending-the-agent---add-a-new-tool) guide

3. **Test thoroughly**
   - Run manual tests with `python main.py`
   - Add unit tests in `tests/` directory
   - Test edge cases and error handling

4. **Update documentation**
   - Add tool description to README
   - Include example usage
   - Document any new dependencies

5. **Commit and push**
   ```bash
   git add .
   git commit -m "Add feature: description of what was added"
   git push origin feature/your-feature-name
   ```

6. **Submit a Pull Request**
   - Clear title and description
   - Reference any related issues
   - Include examples of usage

### Code Standards

- Follow PEP 8 Python style guide
- Add docstrings to all classes and methods
- Keep functions small and focused (single responsibility)
- Use type hints where possible
- Handle errors gracefully (return error messages, don't crash)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

MIT License means you can use this code freely for personal and commercial projects, with the requirement to include the license notice.

## 📚 Resources & References

### Official Documentation
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Google GenAI Python Library](https://github.com/googleapis/python-genai)

### Research Papers & Concepts
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns) (Gang of Four)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)

### Related Projects
- [LangChain](https://github.com/langchain-ai/langchain) - LLM orchestration framework
- [Anthropic's Claude Models](https://www.anthropic.com/) - Alternative LLM provider
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)

## 🎓 Learning Outcomes

By studying this code, you'll learn:

- ✅ How to architect production-ready AI systems
- ✅ Real-world application of SOLID principles
- ✅ Implementation of classic design patterns in Python
- ✅ How to work with LLM function calling APIs
- ✅ Building extensible, maintainable software
- ✅ Multi-turn conversation management
- ✅ Error handling in AI systems

Perfect for software engineers wanting to understand modern AI system architecture!

## 📞 Support & Troubleshooting

### Common Issues

**Problem: `ModuleNotFoundError: No module named 'google.genai'`**
- Solution: Install dependencies: `pip install -r requirements.txt`

**Problem: `KeyError: 'GEMINI_API_KEY'`**
- Solution: Create `.env` file with your API key: `echo "GEMINI_API_KEY=your_key" > .env`

**Problem: Agent responds but doesn't use tools**
- Check: Is your API key valid? Test it at [Google AI Studio](https://aistudio.google.com/)
- Check: Are you using a Gemini model? (Current: gemini-2.5-flash)

**Problem: Tool returns error**
- Check: Tool parameters are correctly formatted
- Check: External APIs (weather, translator) are accessible
- Check: Error handling in tool's execute() method

### Getting Help

1. **Check the code comments** - detailed docstrings explain each component
2. **Review examples** - see how tools are structured in `tools/` directory
3. **Open an issue** - describe problem, include error logs, steps to reproduce
4. **Consult docs** - [Google Gemini docs](https://ai.google.dev/docs) for API questions

### Debug Mode

Add logging to see what's happening:

```python
# In agent.py or main.py
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Now see detailed logs of API calls and tool execution
```

---

**Created with ❤️ to teach clean architecture in AI systems**
