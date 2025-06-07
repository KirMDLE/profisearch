from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base



class MasterProfile(Base):
    __tablename__ = "masters_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    specialization = Column(String, index=True)
    description = Column(Text)

    user = relationship("User", back_populates="master_profile")


