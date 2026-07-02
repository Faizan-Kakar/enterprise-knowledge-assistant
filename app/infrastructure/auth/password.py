from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    # bcrypt only supports up to 72 bytes
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    # bcrypt only supports up to 72 bytes
    # password = password[:72]
    return pwd_context.verify(password, hashed_password)

