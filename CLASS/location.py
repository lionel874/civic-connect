from typing import Optional
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Location(Base):
    __tablename__ = "location"

    id_l: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ville: Mapped[str] = mapped_column(String(20))
    quartier: Mapped[str] = mapped_column(String(20))
    adresse: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)