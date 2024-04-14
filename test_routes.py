"""
Test module for FastAPI User Registration API routes.

This module defines test cases for API routes.

Functions:
    test_register_user: Test case for registering a new user
    test_get_user_by_id: Test case for retrieving user details by user ID
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    """
    Test case for registering a new user.
    """
    payload = {
        "name": "Jhenny",
        "age": 66,
        "gender": "F",
        "ismarried": True,
    }
    response = client.post("/register", json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"

def test_get_user_by_id():
    """
    Test case for retrieving user details by user ID.
    """
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

    response = client.get("/users/999")
    assert response.status_code == 404
