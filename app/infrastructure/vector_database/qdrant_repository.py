from qdrant_client import models
from fastapi import HTTPException, status
from app.infrastructure.vector_database.qdrant_config import client
from qdrant_client.models import Distance, VectorParams, PointStruct, Document
from app.core.exceptions import VectorUpsertError, DeleteDocError

async def initialize_qdrant_collection(collection_name: str, vector_size: int):
    """
    Initializes a Qdrant collection with the specified name and vector size.
    If the collection already exists, it will not be recreated.
    """
    # Check if the collection already exists
    existing_collections = client.get_collections().collections
    if any(col.name == collection_name for col in existing_collections):
        print(f"Collection '{collection_name}' already exists.")
    else:
        # Create a new collection with the specified vector size
        client.recreate_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
        )
        print(f"Collection '{collection_name}' created with vector size {vector_size}.")
    
    client.create_payload_index(
    collection_name="documents",
    field_name="document_name",
    field_schema=models.PayloadSchemaType.KEYWORD,
    )
    client.create_payload_index(
    collection_name="documents",
    field_name="category",
    field_schema=models.PayloadSchemaType.KEYWORD,
    )
    print("Payload indexes for 'document_name' and 'category' created.")
    

async def insert_doc(points):
    try:
        response= client.upsert(
            collection_name="documents",
            points=points
        )
        return response
    except Exception as e:
        raise VectorUpsertError(detail=str(e)) from e
    
async def check_collection(collection_name:str)-> bool:
    
    existing_collections = client.get_collections().collections
    
    if any(col.name == collection_name for col in existing_collections):
        print(f"Collection '{collection_name}' exists.")
        return True
    else:
        return False    

async def check_doc(collection_name:str, document_name:str) -> bool:
    
    # Fetching all docs from the collection
    doc_list = client.facet(
        collection_name=collection_name,
        key="document_name",
    )
    # Checking if doc exists
    if any(doc.value == document_name for doc in doc_list.hits):
        return True
    else:
        return False
         
async def delete_doc(collection_name:str, document_name:str):
    try:
        client.delete(
                    collection_name=collection_name,
                    points_selector=models.FilterSelector(
                        filter=models.Filter(
                            must=[
                                models.FieldCondition(
                                    key="document_name",
                                    match=models.MatchValue(value=document_name)
                                )
                            ]
                        )
                    )   
                )
    except Exception as e:
                raise DeleteDocError(detail = str(e)) from e
    
async def list_doc(collection_name:str):
    doc_list = client.facet(
            collection_name=collection_name,
            key="document_name",
        )

    if doc_list.hits:
        document_names = [doc.value for doc in doc_list.hits]
    else:
            document_names = "No documents found." 
    
    return document_names
        
         
    
    