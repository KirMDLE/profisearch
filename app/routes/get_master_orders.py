###(Роут для получения заказов мастера

from typing import List
from fastapi import APIRouter, Depends, HTTPException, security
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.security import get_current_user
from app.dependencies import get_db


router = APIRouter()

@router.get('/master/{master_id}', dependencies=[Depends(get_current_user)], response_model=List[schemas.OrderRead])
def get_client_orders(master_id: int, db: Session = Depends(get_db)):
    return db.query(models.Order).filter(models.Order.master_id == master_id).all()
