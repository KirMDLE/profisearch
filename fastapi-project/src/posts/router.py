from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from src.posts import schemas, service, dependencies
from src.auth.dependencies import get_current_user

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", response_model=schemas.PostRead)
async def create_post(
    post_create: schemas.PostCreate,
    current_user = Depends(get_current_user),
    db: AsyncSession = Depends(dependencies.get_post_db_session),
):
    post = await service.create_post(db, post_create, author_id=current_user.id)
    return post

@router.get("/{post_id}", response_model=schemas.PostRead)
async def read_post(post_id: int, db: AsyncSession = Depends(dependencies.get_post_db_session)):
    post = await service.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.get("/", response_model=List[schemas.PostRead])
async def read_all_posts(db: AsyncSession = Depends(dependencies.get_post_db_session)):
    result = await db.execute("SELECT * FROM posts")
    posts = result.scalars().all()
    return posts
