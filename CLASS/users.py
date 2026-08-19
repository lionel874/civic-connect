from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database import Base



class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key= True,autoincrement=True)
    nom: Mapped[str] = mapped_column(String(100), nullable=False)
    prenom: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str]= mapped_column(String(50), nullable=False)
    tel:Mapped[int] = mapped_column(Integer, nullable=False)
    role: Mapped[str]= mapped_column(String(15), nullable=False)
        