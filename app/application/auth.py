
from app.infrastructure.database.user_repositories import MongoUserRepository
from app.infrastructure.auth.password import hash_password , verify_password
from app.infrastructure.auth.jwt import create_jwt
from app.domain.entities.user import User

user_repository = MongoUserRepository()

async def signup_service(user):
    
    # checking if user already exists
    existing = await user_repository.find_one(user.userid)
    
    if existing:
        print("User already exists")
        return False
    else:
        # encrypt the password
        hashed_pasword = hash_password(user.password)
        user = User(
            name=user.name,
            userid= user.userid,
            password=hashed_pasword
        )
        # insert into database
        await user_repository.insert_one(user)
        
        return True
    
async def login_service(user):
    
    # Checking if user exists
    existing = await user_repository.find_one(user.userid)
    
    # Get user data
    db_user = await user_repository.get_by_id(user.userid)
    
    if not existing or not verify_password(user.password , db_user["password"]):
        return{"status" : False}       
    else:
        token = create_jwt(user.userid)
        return {
            "status" : True,
            "token" : token
        }
    
    