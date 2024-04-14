"""
Main module for FastAPI User Registration API.

This module initializes the FastAPI application, includes middleware for logging requests,
and includes the user routes.

Attributes:
    app (FastAPI): FastAPI application instance
"""

from fastapi import FastAPI
from middleware import log_request
from routes import users
from database import create_database

app = FastAPI()

@app.middleware("http")
async def middleware(request, call_next):
    """
    Middleware function to log incoming requests.

    Args:
        request (Request): Incoming HTTP request
        call_next (Callable): Next function in the middleware chain

    Returns:
        Response: HTTP response
    """
    response = await log_request(request, call_next)
    return response

app.include_router(users)

@app.on_event("startup")
async def startup_event() -> None:
    """
    Function to create the database on startup.
    """
    create_database()
