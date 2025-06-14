from pydantic import BaseModel

class BaseResponseModel(BaseModel):
    success: bool = True
    message: str | None = None


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")

    from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from src.database import Base  


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False) 
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)  
    recipient_id = Column(Integer, ForeignKey("users.id"), nullable=False)  
    
    rating = Column(Float, nullable=False) 
    comment = Column(String, nullable=True) 
    
    created_at = Column(DateTime, default=datetime.utcnow)

    order = relationship("Order", back_populates="reviews")
    author = relationship("User", foreign_keys=[author_id])
    recipient = relationship("User", foreign_keys=[recipient_id])
