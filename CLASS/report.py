from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from sqlalchemy import ForeignKey,String


class Report(Base) :
    __tablename__ = "report"

    id_r: Mapped[int]=mapped_column(primary_key=True)
    titre: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(100))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    location_id: Mapped[int] = mapped_column(ForeignKey("location.id_l"))
