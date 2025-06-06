###(Роут для получения списка мастеров)

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.dependencies import get_db

router = APIRouter()


@router.get('/', response_model=List[schemas.MasterProfileRead])
def get_list_masters(db: Session = Depends(get_db)):
    profiles = db.query(models.MasterProfile).all()
    return profiles
