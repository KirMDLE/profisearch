from fastapi import FastAPI
from src.auth.router import router as auth_router
from src.posts.router import router as posts_router

app = FastAPI(title="FastAPI Project")

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(posts_router, prefix="/posts", tags=["posts"])

@app.on_event("startup")
async def on_startup():
    print("Application startup")

@app.on_event("shutdown")
async def on_shutdown():
    print("Application shutdown")
