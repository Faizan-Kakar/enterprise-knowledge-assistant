from abc import ABC, abstractmethod
from app.domain.entities.user import User

class UserRepository():
    
    # @abstractmethod
    # async def create(self, user: User) -> User:
    #     pass
    
    @abstractmethod
    async def find_one(self, userid: str) -> User:
        pass
    
    
    @abstractmethod
    async def insert_one(self, user:User) -> User:
        pass
    
    @abstractmethod
    async def get_by_id(self, user:User) -> User:
        pass
    