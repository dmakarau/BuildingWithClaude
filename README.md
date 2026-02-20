# Building with the Claude API

Learning repository for the [Anthropic Academy course](https://anthropic.skilljar.com/claude-with-the-anthropic-api/287735) on building applications with Claude.

## About

This repository contains my code and notes from the "Building with the Claude API" course. The course covers the full spectrum of working with Anthropic models, from basic API usage to advanced agent architectures.

## Course Topics

- **Getting Started with Claude** - API authentication, basic requests, conversation management, system prompts, structured output
- **Prompt Engineering & Evaluation** - Prompting strategies, evaluation frameworks, systematic testing
- **Tool Use with Claude** - Function calling, multi-turn tool interactions, batch tool calling
- **Retrieval Augmented Generation (RAG)** - Text chunking, embeddings, hybrid search, reranking
- **Model Context Protocol (MCP)** - Custom tools and resources, MCP servers and clients
- **Claude Code & Computer Use** - Development workflows, UI automation
- **Agents and Workflows** - Parallel execution, operation chaining, conditional routing

## Prerequisites

- Python 3.x
- Anthropic API key
- Basic knowledge of handling JSON data

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install anthropic python-dotenv
   ```
3. Create a `.env` file with your API key:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

## Helper Module

The `claude_helpers.py` module provides reusable functions and setup for working with the Claude API:

- **Client setup**: Automatically loads environment variables and creates the Anthropic client
- **Helper functions**: `add_user_message()`, `add_assistant_message()`, `chat()`
- **Optional parameters**: System prompts and temperature control in the `chat()` function

Import it in any notebook to avoid duplicating setup code:
```python
from claude_helpers import client, model, add_user_message, add_assistant_message, chat
```

## Notebooks

| File | Description |
|------|-------------|
| [001_requests.ipynb](001_requests.ipynb) | Basic API requests and multi-turn conversations |
| [001_requests_exercise.ipynb](001_requests_exercise.ipynb) | Interactive chat exercise with conversation history |
| [002_system_prompt.ipynb](002_system_prompt.ipynb) | Using system prompts to guide Claude's behavior |
| [003_temperature.ipynb](003_temperature.ipynb) | Exploring temperature parameter for response randomness |
| [004_streaming.ipynb](004_streaming.ipynb) | Streaming responses from Claude API |

## Resources

- [Anthropic API Documentation](https://docs.anthropic.com/)
- [Anthropic Academy](https://anthropic.skilljar.com/)
- [Claude API Reference](https://docs.anthropic.com/en/api)

## License

[MIT](LICENSE)
