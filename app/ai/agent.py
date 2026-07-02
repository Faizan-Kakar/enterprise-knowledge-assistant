from langchain.agents import create_agent
from app.ai.model import model
from app.ai.tools import search_doc
from app.ai.prompts import SYSTEM_PROMPT   
from app.ai.memory import checkpointer


agent = create_agent(
    model=model,
    tools=[search_doc],
    system_prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer,
)

