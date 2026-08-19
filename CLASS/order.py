from sqlalchemy import String,Integer
from sqlalchemy.orm import Mapped,mapped_column
from database import Base
from sqlalchemy import ForeignKey , String
from CLASS.product import Product

class Order(Base):
    __tablename__ = "order"

    num_o: Mapped[int] = mapped_column(primary_key= True, autoincrement= True)
    titre_o: Mapped[str] = mapped_column(String(20))
    quantite_o: Mapped[int] = mapped_column(Integer)
    mte_total: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id_p"))

