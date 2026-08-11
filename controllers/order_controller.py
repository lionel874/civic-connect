from sqlalchemy.orm import Session
from CLASS.order import Order
from database import engine
from CLASS.users import User
from CLASS.product import Product

def ajout_order( nom, quantite, mte, user_id, product_id,db_engine=engine):
    with Session(db_engine) as session:
        user = session.get(User, user_id)

        if user is None:
            raise ValueError("L'utilisateur n'existe pas")

        product = session.get(Product, product_id)

        if product is None:
            raise ValueError("Le produit n'existe pas")




        command = Order(
                        nom_o = nom,
                        quantite_o = quantite,
                        mte_total= mte,
                        user_id = user_id,
                        product_id =product_id
                         )
        session.add(command)
        session.commit()

        return command