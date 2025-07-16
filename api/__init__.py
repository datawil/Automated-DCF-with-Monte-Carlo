from .fastapi_app import app  # Makes the FastAPI app importable
from .cache_config import setup_caching

__all__ = ['app', 'setup_caching']