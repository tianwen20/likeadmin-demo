from typing import Optional

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from starlette.requests import Request
from starlette.responses import Response
import redis
from ..config import get_settings

settings = get_settings()

host = settings.redis_host
port = settings.redis_port
db = settings.redis_default_db
password = settings.redis_password

redis_url = f"redis://{host}:{port}/{db}"

# Redis缓存实例
redis_be: RedisBackend = RedisBackend(
    aioredis.from_url(redis_url, password=password, encoding='utf8', decode_responses=True))

redis_sync = redis.StrictRedis(host=host, port=port, db=db, password=password)


def custom_key_builder(
        func,
        namespace: Optional[str] = "",
        request: Optional[Request] = None,
        response: Optional[Response] = None,
        args: Optional[tuple] = None,
        kwargs: Optional[dict] = None,
):
    """自定义key构造器"""
    key = kwargs.get('key')
    if not key and args:
        key = args[0]
    cache_key = f'{FastAPICache.get_prefix()}{str(key)}'
    return cache_key


def get_key(key: str) -> str:
    """key通用前缀"""
    return f'{get_settings().redis_prefix}{key}'
