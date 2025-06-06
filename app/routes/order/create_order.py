###(создание заказов для мастеров)
import asyncio
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile,BackgroundTasks
from sqlalchemy.orm import Session
from app import models, schemas
from app.dependencies import get_db

router = APIRouter(prefix='/orders', tags=['orders'])

def send_notification(order_id: int):
    return f'Ваш заказ №{order_id} принят!'


@router.post('/create_order')
def create_order(order: schemas.OrderCreate,bg_task: BackgroundTasks, db: Session = Depends(get_db)):
    client = db.query(models.User).filter(models.User.id == order.client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Клиент не найден")
    
    master = db.query(models.MasterProfile).filter(models.MasterProfile.user_id == order.master_id).first()
    if not master:
        raise HTTPException(status_code=404, detail="Мастер не найден")


    new_order = models.Order(
        client_id = client.id,
        master_id = master.id,
        description = order.description,
        
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    bg_task.add_task(send_notification)
    
    #asyncio.create_task(send_notification())

    return {'message':  "Заказ успешно создан"}
