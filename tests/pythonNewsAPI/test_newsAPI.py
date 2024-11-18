import pytest
import logging
from httpx import AsyncClient
from src.pythonNewsAPI.main import app

BASE_URL = "http://127.0.0.1:8000"
logging.basicConfig(level=logging.INFO)

@pytest.mark.asyncio
async def test_stock_news_polygon():
    async with AsyncClient(app=app, base_url = BASE_URL) as ac:
        response = await ac.post("/stock-news-polygon", json={
            "symbol": "AAPL",
            "order": "asc",
            "limit": "5"
        })
    #logging.info(f"Response Content: {response.json()}")
    assert response.status_code == 200
    assert "results" in response.json()

@pytest.mark.asyncio
async def test_stock_news_langchain():
    async with AsyncClient(app=app, base_url = BASE_URL) as ac:
        response = await ac.post("/stock-news-langchain", json={
            "symbol": "AAPL",
            "duration": "today"
        })
    #logging.info(f"Response Content: {response.json()}")
    assert response.status_code == 200
    assert "result" in response.json()

