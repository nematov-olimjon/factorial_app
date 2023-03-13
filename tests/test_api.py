import pytest
import asyncio
from fastapi.testclient import TestClient
from fastapi import WebSocket
from unittest.mock import AsyncMock, patch
from src.main import app, process_data


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def mock_websocket():
    return AsyncMock(spec=WebSocket)


def test_process_data_valid_input():
    result = asyncio.run(process_data("5"))
    assert result == "120"


def test_process_data_invalid_input():
    result = asyncio.run(process_data("hello"))
    assert result == "Error: Invalid input. Please enter a valid integer."



