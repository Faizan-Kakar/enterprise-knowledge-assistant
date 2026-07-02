from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, HTTPBearer

from app.infrastructure.auth.jwt import decode_token
from app.infrastructure.database.user_repositories import MongoUserRepository

from fastapi.security import HTTPAuthorizationCredentials

security = HTTPBearer()

# oauth2_scheme = OAuth2PasswordBearer(
#     tokenUrl="/login"
# )

repository = MongoUserRepository()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    payload = decode_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )

    userid = payload.get("sub")

    if userid is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )

    user = await repository.get_by_id(userid)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Not Found"
        )

    return user