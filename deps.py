"""
Dependency function to get a database session.

This function creates a database engine using the `create_database` function
from the `database` module and initializes a SQLModel session using the engine.

Returns:
    Session: An SQLModel session connected to the SQLite database engine.
"""

from database import create_database
from sqlmodel import Session

async def get_session():
    engine = create_database()
    session = Session(engine)
    return session