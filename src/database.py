import re

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr

from src.config import settings
from src.constants import POSTGRES_INDEXES_NAMING_CONVENTION

engine = create_async_engine(settings.DATABASE_URL)
async_session_maker = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


def resolve_table_name(name: str) -> str:
    """Resolve table names to their mapped names."""
    names = re.split('(?=[A-Z])', name)
    return '_'.join([x.lower() for x in names if x])


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)

    @declared_attr
    def __tablename__(self) -> str:
        return resolve_table_name(self.__name__)
