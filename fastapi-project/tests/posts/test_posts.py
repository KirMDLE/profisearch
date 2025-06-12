from httpx import AsyncClient
import pytest
from src.main import app

@pytest.mark.asyncio
async def test_get_posts():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/posts/")  # или нужный эндпоинт
    assert response.status_code == 200
