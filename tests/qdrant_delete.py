from qdrant_client import QdrantClient
from qdrant_client import models

# from app.infrastructure.vector_database.qdrant_config import client
from qdrant_client import QdrantClient

from app.core.config import QDRANT_API_KEY , QDRANT_URL

# connect to Qdrant Cloud
client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    cloud_inference=True
)

# # print(client.get_collections().collections)

# existing_collections = client.get_collections().collections

# collection_name = "embeddigs"

# if any(col.name == collection_name for col in existing_collections):
#         print(f"Collection '{collection_name}' exists.")
# else:
#     print(f"Collection '{collection_name}' does not exist.")
# # try:
    
#     client.delete(
#         collection_name="documents",
#         points_selector=models.FilterSelector(
#             filter=models.Filter(
#                 must=[
#                     models.FieldCondition(
#                         key="document_name",
#                         match=models.MatchValue(value="company_info.pdf")
#                     )
#                 ]
#             )
#         )
#     )
#     print("Points with document_name 'company_info.pdf' have been deleted.")
# except Exception as e:
#     print(f"An error occurred while deleting points: {e}")  

# collection_info = client.get_collection("documents")
# print(collection_info)

# doc_list = client.facet(
#     collection_name="documents",
#     key="document_name",
# )

# print(f"Document names: {doc_list.hits[0].value if doc_list.hits else 'No documents found.'}")

# for doc in doc_list.hits:
#     print(f"Document Name: {doc.value}, Count: {doc.count}")

from app.ai.tools import search_doc

query = "What is the company about?"    
result = search_doc(query)
print(result)