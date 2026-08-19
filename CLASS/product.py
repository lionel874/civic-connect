from sqlalchemy import String,Float, INTEGER
from sqlalchemy.orm import Mapped,mapped_column
from database import Base

class Product(Base):
    __tablename__ = "product"

    id_p: Mapped[int]= mapped_column(primary_key=True, autoincrement=True)
    nom_p: Mapped[str]= mapped_column(String(15))
    prix_p: Mapped[float]= mapped_column(Float)
    quantite_p: Mapped[int] = mapped_column(INTEGER)