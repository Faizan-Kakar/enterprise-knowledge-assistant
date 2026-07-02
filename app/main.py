from contextlib import asynccontextmanager

from fastapi import FastAPI

# from app.api.routes.webhook import router
from app.api.routes.doc import router as upload_doc_router
from app.infrastructure.vector_database.qdrant_repository import initialize_qdrant_collection
from app.api.routes.chat import router as chat_router
from app.api.routes.auth import auth_router
from app.core.exceptions import AppException
from app.core.exception_handler import app_exception_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    await initialize_qdrant_collection(collection_name="documents", vector_size=1024)
    
    yield
    print("Application shutdown complete.")

from dotenv import load_dotenv
import os

load_dotenv() 

app = FastAPI(lifespan=lifespan)
# app.include_router(router)
app.add_exception_handler(AppException, app_exception_handler)
app.include_router(upload_doc_router)
app.include_router(chat_router)
app.include_router(auth_router)