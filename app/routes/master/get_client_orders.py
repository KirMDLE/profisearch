###(Роут для получения заказов клиента)

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.dependencies import get_db


router = APIRouter()

@router.get('/client/{client_id}', response_model=List[schemas.OrderRead])
def get_client_orders(client_id: int, db: Session = Depends(get_db)):
    return db.query(models.Order).filter(models.Order.client_id == client_id).all()
