import uuid
from app.infrastructure.parser.text_extraction import extract_text_pypdf
from app.application.rag.dto import InjestDocCommand
from app.infrastructure.chunking.chunking import create_chunks
from app.infrastructure.embedding.embeddings import create_embeddings
from qdrant_client.models import PointStruct
from app.infrastructure.vector_database.qdrant_repository import insert_doc

async def injest_doc_service(command : InjestDocCommand):
    
    text =await extract_text_pypdf(command.file.file)
    chunks =await create_chunks(text, command.file.filename, command.file.filename)
    embeddings_result =await create_embeddings(chunks)
    embeddings = embeddings_result.embeddings
    
    points = []
    for index, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload={
                    "document_name": chunk.metadata.get("document_name"),
                    "category": chunk.metadata.get("category"),
                    "text": chunk.page_content,
                    "chunk_index": index
                },
            )
        )
        
    response = await insert_doc(points)
    return response
    # return{
    #     "chunks" : chunks,
    #     "embeddings" : embeddings,
        
    # }