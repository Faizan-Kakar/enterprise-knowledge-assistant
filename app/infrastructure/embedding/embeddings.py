from app.infrastructure.embedding.voyage_config import vo
from app.core.exceptions import CreateEmbeddingError

#### CREATING EMBEDDINGS
async def create_embeddings(chunks):
    document = []
    for chunk in chunks:    
        document.append(chunk.page_content)
    try:   
        result = vo.embed(document, model="voyage-4-large", input_type="document")
    except Exception as e:
        raise CreateEmbeddingError(detail=str(e)) from e
    # return documents_embeddings
    return result
