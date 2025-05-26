from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.patch("/profile", response_model=schemas.UserProfile)
def update_profile(update: schemas.UserUpdate, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    if update.name:
        current_user.name = update.name
    if update.email:
        current_user.email = update.email
    db.commit()
    db.refresh(current_user)
    return current_user
