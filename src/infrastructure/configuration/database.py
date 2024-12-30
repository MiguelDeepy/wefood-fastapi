from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.infrastructure.config.configuration import CONNECTION_SQL

Base = declarative_base()


class Database:
    def __init__(self, connection_url: str = CONNECTION_SQL):
        self._engine = create_async_engine(connection_url, future=True, echo=False)
        self._session_maker = sessionmaker(
            bind=self._engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def __aenter__(self) -> AsyncSession:
        self.session = self._session_maker()
        return self.session

    async def __aexit__(self, exc_type, exc_value, traceback):
        try:
            if exc_type:
                await self.session.rollback()
            else:
                await self.session.commit()
        finally:
            await self.session.close()

    def get_session(self) -> AsyncSession:
        return self._session_maker()

    def get_engine(self):
        return self._engine

    async def close(self):
        await self._engine.dispose()
