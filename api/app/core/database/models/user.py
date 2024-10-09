from sqlalchemy import Column, Integer, String, Boolean
from core.database.models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    user_name = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String,nullable=False)
    is_active = Column(Boolean, default=True)