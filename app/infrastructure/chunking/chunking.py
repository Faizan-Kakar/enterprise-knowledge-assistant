from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.core.exceptions import CreateChunkError

#### SPLIT THE TEXT INTO CHUNKS
# 1. Initialize the splitter with optimal parameters
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,       # Maximum number of characters per chunk
    chunk_overlap=100,     # Overlap between consecutive chunks to preserve context
    length_function=len    # Function used to calculate chunk size
)

async def create_chunks(text, doc_name, category):
    # Convert provided text into a list of LangChain Document objects
    try:
        documents = text_splitter.create_documents(
            texts =[text],
            metadatas=[
                {"document_name": doc_name, "category": category}
            ]     # Metadata for each chunk)
        )
    except Exception as e:
        raise CreateChunkError(detail=str(e)) from e
    
    return documents
