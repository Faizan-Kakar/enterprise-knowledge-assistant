from pydantic import BaseModel

class LoginRequest(BaseModel):
    userid: str
    password: str
    
class SignUpRequest(BaseModel):
    userid: str
    name: str
    password : str