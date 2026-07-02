from fastapi import APIRouter, UploadFile, File, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.infrastructure.vector_database.qdrant_config import client
from qdrant_client import models
from io import BytesIO
from app.infrastructure.auth.dependencies import get_current_user

from app.application.rag.inject_document import injest_doc_service
from app.application.rag.delete_document import delete_doc_service
from app.application.rag.search_documents import list_doc_service
from app.application.rag.dto import InjestDocCommand, DeleteDocCommand
from app.schemas.rag import DeleteDocRequest, ListDocRequest
from app.application.rag.dto import ListDocCommand

router = APIRouter()

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
    
@router.post("/upload_documents")
async def upload_document(file: UploadFile = File(...), current_user=Depends(get_current_user)):
    """
    Endpoint to upload a document, extract its text, split it into chunks, and create embeddings.
    """
    # Validate extension
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are allowed.",
        )
    
    # Validate file has name 
    if not file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Filename is required."
        )
    
        
    # Validate filename contains no spaces
    if " " in file.filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Filename must not contain spaces.",
        )
    
    
    
    contents = await file.read()
    
    if len(contents) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Uploaded file is empty."
        )
        
    # Validate file size
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="Maximum allowed file size is 20 MB.",
        )
    
    
    print(f"Length of content is : {len(contents)}")

    
    # Reset pointer after reading
    await file.seek(0)

    command = InjestDocCommand(
        file = file
    )
    
    result =await injest_doc_service(command)
    
    return {
        "success": True,
        "message": "Document uploaded successfully.",
        "data": result,
    }

@router.get("/list_documents/{collection_name}")
async def list_documents(collection_name: str, current_user=Depends(get_current_user)):
    """
    Endpoint to list all document names in the Qdrant collection.
    """
    
    existing_collections = client.get_collections().collections

    # if any(col.name == collection_name for col in existing_collections):
    #     doc_list = client.facet(
    #         collection_name=collection_name,
    #         key="document_name",
    #     )

    #     if doc_list.hits:
    #         document_names = [doc.value for doc in doc_list.hits]
    #     else:
    #         document_names = "No documents found."
            
    # else:
    #     print(f"Collection '{collection_name}' does not exist.")
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,  
    #         detail=f"Collection '{collection_name}' does not exist."
    #     )
    command = ListDocCommand(
        collection_name=collection_name
    )
    
    response = await list_doc_service(command)

    return {
        "success": True,
        "message": "Documents listed successfully.",
        "data": response,
    }
    
    
    

@router.delete("/delete_document/{collection_name}/{document_name}")
async def delete_document(request:DeleteDocRequest, current_user=Depends(get_current_user)):
     
    command = DeleteDocCommand(
        collection_name=request.collection_name,
        document_name=request.document_name
    )
    
    response =await delete_doc_service(command)
    
    return {
        "success": True,
        "message": "Document deleted successfully.",
        "data": response,
    }
    