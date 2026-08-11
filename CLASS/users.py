from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base



class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key= True,autoincrement=True)
    nom: Mapped[str] = mapped_column(String(100))
    prenom: Mapped[str] = mapped_column(String(100))
    email: Mapped[str]= mapped_column(String(50))
    tel:Mapped[str] = mapped_column(String(15))
    role: Mapped[str]= mapped_column(String(15))
        