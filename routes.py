"""
Routes module for FastAPI User Registration API.

This module defines the API routes for user registration and retrieval.

Routes:
    root: Redirects to the API documentation
    register_user: Endpoint to register a new user
    get_user_by_id: Endpoint to retrieve user details by user ID
"""

from fastapi import UploadFile, APIRouter, HTTPException, Depends
from deps import get_session
from models import User, RegistrationResponse
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError
from fastapi.responses import RedirectResponse
from typing import Annotated
import uuid

users = APIRouter()

@users.get('/')
async def root():
    """
    Redirects to the API documentation.
    """
    return RedirectResponse('/docs')

@users.post("/register", response_model=RegistrationResponse)
async def register_user(name: str, age: int, gender: str, ismarried: bool,
                        session: Annotated[Session, Depends(get_session)]):
    """
    Endpoint to register a new user.

    Args:
        name (str): Name of the user
        age (int): Age of the user
        gender (str): Gender of the user
        ismarried (bool): Marital status of the user
        session (Session): Database session

    Returns:
        RegistrationResponse: Response indicating successful user registration
    """
    try:
        user = User(name=name, age=age, gender=gender, is_married=ismarried)
        session.add(user)
        session.commit()
    except IntegrityError:
        raise HTTPException(status_code=400, detail="User already exists")
    return RegistrationResponse(user=user)

@users.get("/users/{user_id}", response_model=User)
async def get_user_by_id(user_id: int, session: Annotated[Session, Depends(get_session)]):
    """
    Endpoint to retrieve user details by user ID.

    Args:
        user_id (int): User ID
        session (Session): Database session

    Returns:
        User: User details
    """
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
