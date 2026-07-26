from sqlalchemy import create_async_engine, async_sessionmaker
from app.core.config import settings

engine = create_async_engine(
    settings.database_url,
    pool_size=settings.pool_size,
    max_overflow=settings.max_overflow,
    pool_timeout=settings.pool_timeout,
    pool_pre_ping=settings.pool_pre_ping,
    pool_recycle=settings.pool_recycle
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False

)

