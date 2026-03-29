# Architecting an Adaptive AI Agent using Design Patterns

A production-ready AI agent framework that demonstrates how to architect adaptive AI systems using proven design patterns. This project showcases the implementation of the **ReAct (Reason-Act-Observe)** loop pattern combined with classic software design patterns like **Factory**, **Registry**, and **Strategy**.

## 🎯 Overview

This project implements an intelligent personal assistant that can:
- Reason about user requests using Google Gemini AI
- Execute multiple tools dynamically without hardcoding
- Maintain conversation memory across multiple turns
- Handle complex multi-step tasks through agentic reasoning
- Extend functionality by adding new tools without modifying core code

## 🏗️ Architecture & Design Patterns

### Core Patterns

| Pattern | Usage | Benefit |
|---------|-------|---------|
| **ReAct Loop** | Reason → Act → Observe cycle for agent decision-making | Transparent reasoning, multi-step problem solving |
| **Factory Pattern** | Tool creation and management | Loose coupling, easy tool addition |
| **Registry Pattern** | Dynamic tool registration and dispatch | No hardcoded if-else chains, scalability |
| **Strategy Pattern** | Different tool implementations with common interface | Polymorphic tool execution |
| **Single Responsibility** | Separate concerns: Agent, Tools, Memory, Registry | Maintainability and testability |

## 📋 Features

- ✅ **Multi-Tool Support**: Execute calculations, translations, weather lookups, time queries
- ✅ **Agentic Reasoning**: AI determines which tools to use and when
- ✅ **Conversation Memory**: Maintains context across multiple turns
- ✅ **Extensible Design**: Add new tools with minimal code changes
- ✅ **Google Gemini Integration**: Leverages state-of-the-art language models
- ✅ **Interactive CLI**: User-friendly command-line interface

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Gemini API key (get one at [Google AI Studio](https://aistudio.google.com/app/apikeys))

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Architecting-an-Adaptive-AI-Agent-using-Design-Patterns
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your Google Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

### Usage

Run the interactive CLI:
```bash
python main.py
```

Example interactions:
```
You: What's 25 + 17?
🤖: The sum of 25 and 17 is 42.

You: What time is it?
🤖: The current time is 3:45 PM.

You: Translate "Hello World" to Spanish
🤖: "Hello World" in Spanish is "Hola Mundo".

You: What's the weather like in New York?
🤖: The weather in New York is...
```

## 📁 Project Structure

```
.
├── agent.py                 # ReAct loop implementation with Gemini integration
├── base_tool.py            # Abstract base class for all tools
├── tool_registry.py        # Factory/Registry pattern for tool management
├── memory_manager.py       # Conversation history management
├── main.py                 # CLI entry point
├── requirements.txt        # Python dependencies
├── tools/                  # Tool implementations
│   ├── __init__.py
│   ├── calculator_tool.py  # Mathematical calculations
│   ├── time_tool.py        # Current time queries
│   ├── weather_tool.py     # Weather information lookup
│   └── translator_tool.py  # Text translation
└── README.md
```

## 🛠️ Available Tools

### Calculator Tool
Performs mathematical calculations (addition, subtraction, multiplication, division)
```python
# Automatically invoked for math queries
User: "Calculate 100 * 2.5"
```

### Time Tool
Retrieves current date and time information
```python
User: "What's the current time?"
```

### Weather Tool
Fetches weather information for locations
```python
User: "What's the weather in Tokyo?"
```

### Translator Tool
Translates text between languages
```python
User: "Translate 'How are you?' to French"
```

## 🧠 How It Works

### The ReAct Loop

```
1. REASON: User input → Gemini analyzes the request
2. ACT: Model determines which tool(s) to call
3. OBSERVE: Tool results returned to the model
4. LOOP: If more steps needed, repeat; else return final answer
```

### Execution Flow

1. User input is passed to the Agent
2. Agent sends input to Gemini with available tools
3. Gemini decides which tool to use (or if no tool is needed)
4. Agent executes the tool via ToolRegistry
5. Results are fed back to Gemini
6. Process repeats until model returns final answer
7. Conversation is stored in MemoryManager

## 🔧 Extending the Agent

### Add a New Tool

1. **Create a new tool class** in `tools/` directory:
   ```python
   # tools/currency_tool.py
   from base_tool import BaseTool
   from google.genai import types
   
   class CurrencyTool(BaseTool):
       def get_name(self) -> str:
           return "convert_currency"
       
       def get_description(self) -> str:
           return "Convert between currencies"
       
       def get_parameters(self) -> types.Schema:
           return types.Schema(
               type=types.Type.OBJECT,
               properties={
                   "amount": types.Schema(type=types.Type.NUMBER),
                   "from_currency": types.Schema(type=types.Type.STRING),
                   "to_currency": types.Schema(type=types.Type.STRING),
               },
               required=["amount", "from_currency", "to_currency"],
           )
       
       def execute(self, **kwargs) -> str:
           # Implement conversion logic
           return f"Conversion result..."
   ```

2. **Register the tool** in `main.py`:
   ```python
   from tools.currency_tool import CurrencyTool
   
   registry.register("convert_currency", CurrencyTool())
   ```

That's it! The agent now has access to currency conversion.

## 📦 Dependencies

- **google-genai**: Google Gemini API client
- **python-dotenv**: Environment variable management
- **requests**: HTTP library for external APIs

See [requirements.txt](requirements.txt) for detailed versions.

## 🔐 Environment Configuration

Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_actual_api_key_here
```

**Never commit `.env` to version control!**

## 💡 Design Principles Applied

- **Open/Closed Principle**: Open for extension (new tools), closed for modification
- **Dependency Inversion**: Depend on abstractions (BaseTool), not concrete implementations
- **Single Responsibility**: Each class has one reason to change
- **Don't Repeat Yourself (DRY)**: Common tool behavior in BaseTool

## 🧪 Testing

To test the agent locally:
```bash
python main.py
# Try various queries to test different tools
```

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### To add a new tool:
1. Follow the "Extending the Agent" section
2. Add tests for your tool
3. Update this README with tool documentation
4. Submit a PR

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 📚 References

- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns)

## 🎓 Learning Resources

This project demonstrates:
- How to structure AI agents for production use
- Implementation of classic design patterns in Python
- Google Gemini's function calling capabilities
- Building extensible, maintainable AI systems

Perfect for learning software architecture alongside AI integration!

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation and examples
- Consult the agent code comments for implementation details

---

**Built with ❤️ to demonstrate clean architecture in AI systems**
