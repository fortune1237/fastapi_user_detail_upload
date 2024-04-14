"""
Database module for FastAPI User Registration API.

This module defines the function to create the SQLite database.

Functions:
    create_database: Function to create the SQLite database
"""

from sqlmodel import SQLModel, create_engine

def create_database():
    """
    Function to create the SQLite database.

    Returns:
        Engine: Database engine
    """
    sqlite_file_name = "database.sqlite"
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    engine = create_engine(sqlite_url, echo=True)
    SQLModel.metadata.create_all(engine)
    return engine
