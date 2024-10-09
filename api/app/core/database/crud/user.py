from sqlalchemy.orm import Session
from sqlalchemy import or_
from functools import lru_cache

from core.database.models import User
from core.database.schemas.user import UserCreate, UserUpdate 

class UserCRUD:

    def get_user_by_id(self, database_session: Session, id: int):
        user = (
            database_session
            .query(User)
            .filter(User.id == id)
            .first()
        )
        return user
    
    def get_user_by_email(self, database_session: Session, email: str):
        user = (
            database_session
            .query(User)
            .filter(User.email == email)
            .first()
        )
        return user
    
    def get_user_by_name(self, database_session: Session, user_name: str):
        user = (
            database_session
            .query(User)
            .filter(User.user_name == user_name)
            .first()
        )
        return user
    
    def get_users(self, database_session: Session, offset: int=0, limit: int=100):
        users = (
            database_session
            .query(User)
            .offset(offset=offset)
            .limit(limit=limit)
            .all()
        )
        return users
    
    def get_all_users(self, database_session: Session):
        users = (
            database_session
            .query(User)
            .all()
        )
        return users
    
    # def create_user(self, database_session: Session, user: UserCreate):
    #     user_in_db = (
    #         database_session
    #         .query(User)
    #         .filter(
    #             or_(
    #                 User.user_name == user.user_name,
    #                 User.email == user.email
    #             )
    #         )
    #         .first()
    #     )

    #     if user_in_db:
    #         return False
        
    #     hashed_password = 

@lru_cache
def get_user_crud():
    return UserCRUD()