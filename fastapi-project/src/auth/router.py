from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.auth import schemas, service
from src.database import AsyncSessionLocal

router = APIRouter()

def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup", response_model=schemas.UserRead)
def signup(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user_data)

@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return service.authenticate_user(db, form_data.username, form_data.password)
