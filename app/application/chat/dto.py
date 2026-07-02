from dataclasses import dataclass


@dataclass
class ChatCommand:
    query:str
    chat_id:int
