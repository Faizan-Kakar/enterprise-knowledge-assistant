from app.application.rag.dto import DeleteDocCommand
from app.infrastructure.vector_database.qdrant_repository import check_collection, check_doc, delete_doc
from fastapi import HTTPException, status

async def delete_doc_service(request : DeleteDocCommand):
    
    if await check_collection(request.collection_name):
        
        if await check_doc(request.collection_name,request.document_name):
            response =await delete_doc(request.collection_name, request.document_name)
            return response
            
        else:
            raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,  
                    detail=f"Document '{request.document_name}' does not exist in collection '{request.collection_name}'."
                ) 
    else:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,  
                detail=f"Collection '{request.collection_name}' does not exist."
            )    