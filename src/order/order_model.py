from enum import Enum  
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text, Enum as SQLEnum
from app.database import Base
import datetime

class OrderStatus(Enum):
    new = 'new' 
    in_progress = 'in_progress'
    completed = 'completed'
    cancelled = 'cancelled'


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("users.id"))
    master_id = Column(Integer, ForeignKey("masters_profiles.id"))
    description = Column(Text)
    
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    status = Column(SQLEnum(OrderStatus), default=OrderStatus.new) 

