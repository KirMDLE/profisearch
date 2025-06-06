from enum import Enum
import enum
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class UserRole(str, enum.Enum):
    client = "client"
    master = "master"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(UserRole), nullable=False)

    master_profile = relationship("MasterProfile", back_populates="user", uselist=False)
