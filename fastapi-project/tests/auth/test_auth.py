from httpx import AsyncClient
import pytest
from src.main import app

@pytest.mark.asyncio
async def test_healthcheck_auth():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/auth/healthcheck")  # или другой простой эндпоинт auth
    assert response.status_code == 200
