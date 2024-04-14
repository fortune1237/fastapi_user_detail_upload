"""
Models module for FastAPI User Registration API.

This module defines the data models used in the API.

Classes:
    UserCreate: Data model for creating a new user
    User: Data model for user details
    RegistrationResponse: Response model for user registration
"""

from sqlmodel import SQLModel, Field
from pydantic import BaseModel

class UserCreate(SQLModel):
    """
    Data model for creating a new user.

    Attributes:
        name (str): Name of the user
        age (int): Age of the user
        gender (str): Gender of the user
        is_married (bool): Marital status of the user
    """
    name: str = Field(min_length=3, max_length=50, description="Name of the user")
    age: int = Field(min_length=1, max_length=3, description="Age of the user")
    gender: str = Field(description="Gender of the user")
    is_married: bool = Field(description="Marital status of the user")

class User(UserCreate, table=True):
    """
    Data model for user details.

    Attributes:
        id (int | None): User ID (primary key)
    """
    id: int | None = Field(default=None, primary_key=True)

class RegistrationResponse(BaseModel):
    """
    Response model for user registration.

    Attributes:
        message (str): Message indicating successful user registration
    """
    message: str = "User registered successfully"
