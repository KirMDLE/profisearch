###(Роут для получения заказов мастера

from typing import List
from fastapi import APIRouter, Depends, HTTPException, security
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


@router.get('/master/{master_id}',dependencies=[Depends(security.access_token_required)], response_model=List[schemas.OrderRead])
def get_client_orders(master_id: int, db: Session = Depends(get_db)):
    return db.query(models.Order).filter(models.Order.master_id == master_id).all()
