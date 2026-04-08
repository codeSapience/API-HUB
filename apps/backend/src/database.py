from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from src.config import settings

engine = create_async_engine(
    settings.DATABASE_URL, echo=settings.DEBUG, pool_size=10, max_overflow=20
)

AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


# Import all models so Alembic can discover them
from src.models import User, APIVariant, Subscription, UsageRecord
