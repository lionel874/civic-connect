from sqlalchemy.orm import Session
from database import engine,Base
from controllers.order_controller import ajout_order
from CLASS.order import Order
from CLASS.product import Product
from CLASS.users import User

ajout_order("commande-1",
            " 15 article",
            "25.00fcfa",
            1,1)
with Session(engine) as session:
    commande = session.query(Order).filter_by(product_id = 1).first()
    assert commande is not None
    assert commande.nom_o == "commande-1"
    assert commande.quantite_o == "15 article"
    assert commande.mte_total =="25.000fcfa"
    assert commande.user_id ==1
    assert commande.product_id == 1
    
