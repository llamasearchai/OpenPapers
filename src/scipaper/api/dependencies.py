"""API dependencies for authentication."""

from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from loguru import logger

security = HTTPBearer()

async def api_key_auth(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> Optional[str]:
    """API key authentication dependency."""
    if not credentials or not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    api_key = credentials.credentials
    # In production, implement proper API key validation
    # For now, accept any non-empty API key
    if not api_key or len(api_key.strip()) == 0:
        logger.warning("Empty API key provided")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    logger.info("API key authenticated for request")
    return api_key
