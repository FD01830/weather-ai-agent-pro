from langchain_openai import ChatOpenAI
from config import (
    XAI_API_KEY,
    XAI_BASE_URL,
    MODEL_NAME,
)

from tools import get_weather

# Initialize Grok via xAI's OpenAI-compatible API
llm = ChatOpenAI(
    api_key=XAI_API_KEY,
    base_url=XAI_BASE_URL,
    model=MODEL_NAME,
    temperature=0
)

# Register tools
tools = [
    get_weather
]

# Bind tools to the model
llm_with_tools = llm.bind_tools(tools)
