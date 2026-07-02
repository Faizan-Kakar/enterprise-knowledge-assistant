from langchain.chat_models import init_chat_model
from app.core.config import ANTHROPIC_API_KEY


# model = init_chat_model(
#     "claude-sonnet-4-6",
#     temperature=0.5,
#     timeout=600,
#     max_tokens=25000,
#     streaming=True,
# )

from langchain_ollama import ChatOllama

model = ChatOllama(
    model="llama3.1:latest",
    # model="gemma3:4b",
    temperature=0.5,
    num_predict=512,
    streaming=True,
)

