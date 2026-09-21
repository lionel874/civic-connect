from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class PointConnectivite(Base):
    __tablename__ = "point_connectivite"

    id_pc: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nom: Mapped[str] = mapped_column(String(50))
    qualite_reseau: Mapped[str] = mapped_column(String(20))
    horaires: Mapped[str] = mapped_column(String(50))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    location_id: Mapped[int] = mapped_column(ForeignKey("location.id_l"))