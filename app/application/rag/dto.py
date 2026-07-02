from dataclasses import dataclass
from fastapi import File, UploadFile

@dataclass 
class InjestDocCommand:
    file : File

    
@dataclass 
class DeleteDocCommand:
    collection_name : str
    document_name : str
    
@dataclass 
class ListDocCommand:
    collection_name : str
    

