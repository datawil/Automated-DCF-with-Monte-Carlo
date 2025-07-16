from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache

def setup_caching():
    FastAPICache.init(InMemoryBackend())

@cache()
async def get_cache():
    """Utility function for cache management"""
    return FastAPICache.get_backend()