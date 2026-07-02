from qdrant_client import QdrantClient

from app.core.config import QDRANT_API_KEY , QDRANT_URL

# connect to Qdrant Cloud
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    cloud_inference=True
)