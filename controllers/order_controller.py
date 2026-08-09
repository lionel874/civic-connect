from sqlalchemy.orm import Session
from CLASS.order import Order
from database import engine

def ajout_order( nom, quantite, mte, user_id, product_id):
    with Session(engine) as session:
        command = Order(
                        nom_o = nom,
                        quantite_o = quantite,
                        mte_total= mte,
                        user_id = user_id,
                        product_id =product_id
                         )
        session.add(command)
        session.commit()