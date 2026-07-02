from app.infrastructure.vector_database.qdrant_repository import check_collection, list_doc
from app.core.exceptions import ListDocError
from fastapi import HTTPException, status
from app.application.rag.dto import ListDocCommand

async def list_doc_service(request: ListDocCommand):
    
    if await check_collection(request.collection_name):
        try:
            response = await list_doc(request.collection_name)
            return response
        except Exception as e:
                raise ListDocError(detail = str(e)) from e
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,  
                detail=f"Collection '{request.collection_name}' does not exist."
            )