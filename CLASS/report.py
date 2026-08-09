from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
from sqlalchemy import ForeignKey,String

class Report :
    __tablename__ = "report"

    id_r: Mapped[int]=mapped_column(primary_key=True)
    titre: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(String(50))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    location_id: Mapped[int] = mapped_column(ForeignKey("loxation.id"))
