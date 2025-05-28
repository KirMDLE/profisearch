from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.security import get_current_user
from app.dependencies import get_db

router = APIRouter()


@router.post("/make_master/{user_id}")
def make_master(user_id: int, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Только админ может менять роли")

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    user.role = "master"
    db.commit()
    return {"message": f"Пользователь {user.email} теперь мастер"}