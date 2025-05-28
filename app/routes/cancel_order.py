from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.security import get_current_user
from app.dependencies import get_db

router = APIRouter()

@router.post("/orders/{order_id}/cancel")
def cancel_order(order_id: int, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.role != "client":
        raise HTTPException(status_code=403, detail="Только клиент может отменить заказ")

    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order or order.client_id != current_user.id:
        raise HTTPException(status_code=404, detail="Заказ не найден или не принадлежит вам")

    if order.status != "new":
        raise HTTPException(status_code=400, detail="Нельзя отменить заказ, который уже принят")

    order.status = "cancelled"
    db.commit()
    return {"message": "Заказ отменён"}        