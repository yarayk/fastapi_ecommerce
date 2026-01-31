import decimal
from decimal import Decimal
from datetime import datetime
from typing import List
from xmlrpc.client import DateTime
from sqlalchemy import func

from sqlalchemy import create_engine, String, Numeric, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, relationship

# Строка подключения для SQLite
DATABASE_URL = "sqlite:///ecommerce.db"

# Создаём Engine
engine = create_engine(DATABASE_URL, echo=True)
# Настраиваем фабрику сеансов
SessionLocal = sessionmaker(bind=engine)

# Определяем базовый класс для моделей
class Base(DeclarativeBase):
    pass

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    start_time: Mapped[datetime] = mapped_column(nullable=False)
    end_time: Mapped[datetime | None]
    description: Mapped[str] = mapped_column(Text)

