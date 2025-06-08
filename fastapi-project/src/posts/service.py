from sqlalchemy.ext.asyncio import AsyncSession
from src.posts import models, schemas

async def create_post(db: AsyncSession, post_create: schemas.PostCreate, author_id: int) -> models.Post:
    new_post = models.Post(
        title=post_create.title,
        content=post_create.content,
        author_id=author_id
    )
    db.add(new_post)
    await db.commit()
    await db.refresh(new_post)
    return new_post

async def get_post(db: AsyncSession, post_id: int):
    result = await db.get(models.Post, post_id)
    return result
