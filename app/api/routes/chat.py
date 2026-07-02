from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends
from app.ai.agent import agent
from pydantic import BaseModel
from app.infrastructure.auth.dependencies import get_current_user
from app.application.chat.chat_service import chat
from app.application.chat.dto import ChatCommand

router = APIRouter()

class QuestionRequest(BaseModel):
    query: str
    chat_id: int

@router.post("/ask")
async def ask_question(request: QuestionRequest, current_user= Depends(get_current_user)):
    """
    Endpoint to ask a question and get an answer.
    """
    command = ChatCommand(
        query=request.query,
        chat_id=request.chat_id
    )
    
    response = await chat(command)
    
    return {
        "success": True,
        "message": "Question answered successfully.",
        "question": request.query,
        "answer": response["messages"][-1].content,
        }
    