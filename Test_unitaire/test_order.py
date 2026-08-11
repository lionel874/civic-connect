from sqlalchemy.orm import Session
from database import engine,Base
from controllers.order_controller import ajout_order
from CLASS.order import Order
from CLASS.product import Product
from CLASS.users import User
from sqlalchemy import create_engine
import unittest

test_engine = create_engine(
    "sqlite:///test_database/test_civic_connect.db"
)
Base.metadata.create_all(test_engine)


class TestAjoutOrder(unittest.TestCase):

 def test_order_valide(self):

    # 1. Créer un utilisateur pour le test
    user = User(
        nom="moudouthe",
        prenom="lionel",
        email="lionel@gmail.com",
        tel="680048703",
        role="admin"
    )

    # 2. Créer un produit pour le test
    product = Product(
        nom_p="produit-1",
        prix_p="1000 fcfa",
        quantite_p="10"
    )

    # 3. Ajouter User et Product dans la base de test
    with Session(test_engine) as session:
        session.add(user)
        session.add(product)
        session.commit()

      
if __name__ == "__main__":
    unittest.main()