import urllib.error
import urllib.request

from langchain.tools import tool
from app.infrastructure.embedding.voyage_config import vo
from app.infrastructure.vector_database.qdrant_config import client 


@tool
def search_doc(query: str) -> str:
    """
    Search the company's knowledge base.

    Use this tool whenever the user asks about:
    - Company policies
    - Internal documents
    - Uploaded files
    - Business-specific information
    - Information that may not be in your training data

    Do not use this tool for general knowledge questions.
    """
    # Placeholder implementation - replace with actual search logic
    querry_embeddings = vo.embed([query], model="voyage-4-large", input_type="query")
    # querry_embeddings = ""
    
    results = client.query_points(
        collection_name="documents",
        query=querry_embeddings.embeddings[0],
        with_payload=True,
        with_vectors=True,
        limit=1
    )
    return results.points[0].payload["text"]