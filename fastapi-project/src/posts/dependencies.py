from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from src.database import get_async_session

async def get_post_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with get_async_session() as session:
        yield session
