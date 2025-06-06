from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.security import get_current_user
from app.dependencies import get_db

router = APIRouter()

@router.post("/orders/{order_id}/accept")
def accept_order(order_id: int, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.role != "master":
        raise HTTPException(status_code=403, detail="Только мастер может принять заказ")

    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Orded not found")

    if order.status != "new":
        raise HTTPException(status_code=400, detail="Заказ уже обработан")

    order.status = "accepted"
    order.master_id = current_user.id
    db.commit()
    return {"message": "Заказ принят"}