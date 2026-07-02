from pydantic import BaseModel

class ExtractionResponse(BaseModel):
    answer: str