from app.application.chat.dto import ChatCommand
from app.ai.agent import agent
from app.core.exceptions import AgentExecutionError


async def chat(command:ChatCommand):
    try:
        response = agent.invoke(
            {"messages": [{"role": "user", "content": command.query}]},
            config={"configurable": {"thread_id": f"chat_thread_{command.chat_id}"}}  # Example of passing a thread ID for conversation context
        )
        return response
    except Exception as e:
        raise AgentExecutionError(detail=str(e)) from e
    