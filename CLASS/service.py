from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from sqlalchemy import ForeignKey

class Service(Base) :
    __tablename__ = "service"

    id_s: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    nom_s: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(String(50))
    prix: Mapped[str] = mapped_column (String(10))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    location_id: Mapped[int]= mapped_column(ForeignKey("location.id_l"))