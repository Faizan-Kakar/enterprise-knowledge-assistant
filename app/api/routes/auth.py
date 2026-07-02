from fastapi import FastAPI, APIRouter, HTTPException, Depends
from pydantic import BaseModel , EmailStr
from app.application.auth import signup_service, login_service
from app.schemas.auth import SignUpRequest, LoginRequest
from fastapi.security import OAuth2PasswordRequestForm

auth_router =  APIRouter() 

@auth_router.post("/signUp")
async def signUp(user : SignUpRequest):
    
    response =await signup_service(user)
    
    if response:
        return {
            "success": True,
            "message": "User successfully signed in",
        }
    else:
        return{
            "success": False,
            "message": "User Already Exist"
        }
         

@auth_router.post("/login")
async def login(user : LoginRequest):
    
    response = await login_service(user)
    
    if response["status"]:
        return {
        "success": True,
        "token" : response["token"],
        "message": "User LogedIn",
        }
    else:
       return{
            "success": False,
            "message": "Invalid Credentials"
        }