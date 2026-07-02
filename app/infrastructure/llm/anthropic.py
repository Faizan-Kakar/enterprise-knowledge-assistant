from langchain_anthropic import ChatAnthropic
from app.core.config import ANTHROPIC_API_KEY

# llm = ChatAnthropic(
#     # model_name="claude-3-5-sonnet-latest",
#     model_name="claude-3-7-sonnet-latest",
#     api_key=ANTHROPIC_API_KEY
# )

llm = ChatAnthropic(
    model="claude-haiku-4-5-20251001",
    api_key=ANTHROPIC_API_KEY,
    # temperature=,
    # max_tokens=,
    # timeout=,
    # max_retries=,
    # ...
)
