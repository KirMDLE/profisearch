from contextlib import contextmanager
from typing import Generator
from sqlalchemy.orm import Session
from src.database import SessionLocal

@contextmanager
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
