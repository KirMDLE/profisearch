from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from src.auth import models, schemas, utils
from src.auth.exceptions import UserAlreadyExistsException, InvalidCredentialsException

def create_user(db: Session, user_data: schemas.UserCreate):
    existing_user = db.query(models.User).filter(models.User.email == user_data.email).first()
    if existing_user:
        raise UserAlreadyExistsException()
    
    hashed_password = utils.hash_password(user_data.password)
    new_user = models.User(email=user_data.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user or not utils.verify_password(password, user.hashed_password):
        raise InvalidCredentialsException()
    
    access_token = utils.create_access_token(data={"sub": user.email})
    return schemas.Token(access_token=access_token, token_type="bearer")


SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"


async def verify_token(token: str) -> int:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = int(payload.get("sub"))
        if user_id is None:
            raise ValueError("Token payload missing 'sub'")
        return user_id
    except (JWTError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )


async def get_user_by_id(user_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(models.User).where(models.User.id == user_id))
        return result.scalar_one_or_none()
