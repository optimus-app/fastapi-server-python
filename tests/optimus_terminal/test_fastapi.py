from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from optimus_terminal.fast_api.main import app  # Import your FastAPI app

client = TestClient(app)


def test_stock_news_polygon():
    payload = {"symbol": "AAPL", "order": "asc", "limit": "5"}

    response = client.post("/stock-news-polygon", json=payload)
    response_data = response.json()

    assert response.status_code == 200
    assert "results" in response_data
    assert isinstance(response_data["results"], list)

    if response_data["results"]:  # If there are results
        first_result = response_data["results"][0]
        assert "id" in first_result
        assert "publisher" in first_result
        assert "title" in first_result


def test_stock_price_api():
    with patch("optimus_terminal.fast_api.main.requests.get") as mock_requests_get:
        mock_requests_get.return_value.status_code = 200
        response = client.get("/stock-price/aapl?period=1d")
        response_data = response.json()

        assert response.status_code == 200

        assert "symbol" in response_data
        assert "entries" in response_data

        assert isinstance(response_data["symbol"], str)
        assert isinstance(response_data["entries"], list)

        for entry in response_data["entries"]:
            assert set(entry.keys()) == {
                "date",
                "open",
                "high",
                "low",
                "close",
                "volume",
            }
            assert isinstance(entry["date"], str)
            assert isinstance(entry["open"], (int, float))
            assert isinstance(entry["high"], (int, float))
            assert isinstance(entry["low"], (int, float))
            assert isinstance(entry["close"], (int, float))
            assert isinstance(entry["volume"], int)


def test_stock_news_langchain():
    with patch("optimus_terminal.fast_api.main.requests.get") as mock_requests_get:
        payload = {"symbol": "AAPL"}

        mock_requests_get.return_value.status_code = 200
        response = client.post("/stock-news-langchain", json=payload)

        assert response.status_code == 200
        assert "result" in response.json()
        assert isinstance(response.json().get("result"), str)
