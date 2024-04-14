"""
Middleware module for FastAPI User Registration API.

This module defines the middleware function for logging requests.

Functions:
    log_request: Middleware function to log incoming requests
"""

from venv import logger
from fastapi import Request
import logging
import sys
import time

async def log_request(request: Request, call_next):
    """
    Middleware function to log incoming requests.

    Args:
        request (Request): Incoming HTTP request
        call_next (Callable): Next function in the middleware chain

    Returns:
        Response: HTTP response
    """
    start = time.time()
    response = await call_next(request)
    process_time = time.time() - start
    log_dict = {
        "url": request.url.path,
        "method": request.method,
        "process_time": process_time,
        "host": request.client.host,
        "ip": request.client.host
    }
    logger.info(log_dict, extra=log_dict)

    return response
