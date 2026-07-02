from pydantic import BaseModel
from fastapi import UploadFile

class DeleteDocRequest(BaseModel):
    collection_name : str
    document_name : str
    
class ListDocRequest(BaseModel):
    collection_name : str
    