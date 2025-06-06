from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.security import get_current_user
from app.dependencies import get_db

router = APIRouter()

@router.get("/me", response_model=schemas.UserProfile)
def get_my_profile(current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    return current_user
