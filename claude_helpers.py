"""
Helper functions and client setup for working with Claude API
"""
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables
load_dotenv()

# Create API client
client = Anthropic()
model = "claude-sonnet-4-5-20250929"


def add_user_message(messages, text):
    """Add a user message to the messages list"""
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    """Add an assistant message to the messages list"""
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(messages, system_prompt=None, temperature=None):
    """Send messages to Claude and get a response"""
    kwargs = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    
    if system_prompt:
        kwargs["system"] = system_prompt
    if temperature:
        kwargs["temperature"] = temperature
    
    message = client.messages.create(**kwargs)
    return message.content[0].text
