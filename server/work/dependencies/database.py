from databases import Database

from ..config import get_settings

__all__ = ['db', 'database_url']

settings = get_settings()
database_url = f"mysql+pymysql://{settings.database_user}:{settings.database_password}@{settings.database_host}:{settings.database_port}/{settings.database_name}?charset=utf8mb4"

# 数据库实例
db: Database = Database(
    database_url,
    min_size=settings.database_pool_min_size,
    max_size=settings.database_pool_max_size,
    pool_recycle=settings.database_pool_recycle)
