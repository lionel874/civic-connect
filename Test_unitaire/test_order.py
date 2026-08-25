import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from database import Base

from CLASS.users import User
from CLASS.product import Product
from CLASS.order import Order

from SERVICES.order_service import (
    ajout_order,
    lire_order_service
)


test_engine = create_engine(
    "sqlite:///test_database/test_civic_connect.db"
)

Base.metadata.create_all(test_engine)


class TestOrderService(unittest.TestCase):

    # Test ajout d'une commande valide

    def test_ajout_order_valide(self):

        with Session(test_engine) as session:

            utilisateur = User(
                nom="moudouthe",
                prenom="lionel",
                email="order@gmail.com",
                tel="680048703",
                role="user"
            )

            produit = Product(
                nom_p="produit1",
                prix_p=1000,
                quantite_p=10
            )

            session.add(utilisateur)
            session.add(produit)
            session.commit()

            commande = ajout_order(
                "commande1",
                5,
                utilisateur.id,
                produit.id_p,
                session
            )

            self.assertIsNotNone(commande)

            self.assertEqual(
                commande.titre_o,
                "commande1"
            )

            self.assertEqual(
                commande.quantite_o,
                5
            )

            self.assertEqual(
                commande.mte_total,
                5000
            )


    # Test titre vide

    def test_titre_vide(self):

        with Session(test_engine) as session:

            with self.assertRaises(ValueError):

                ajout_order(
                    "",
                    5,
                    1,
                    1,
                    session
                )


    # Test titre None

    def test_titre_none(self):

        with Session(test_engine) as session:

            with self.assertRaises(ValueError):

                ajout_order(
                    None,
                    5,
                    1,
                    1,
                    session
                )


    # Test titre qui n'est pas une chaîne

    def test_titre_n_est_pas_une_chaine(self):

        with Session(test_engine) as session:

            with self.assertRaises(ValueError):

                ajout_order(
                    123,
                    5,
                    1,
                    1,
                    session
                )


    # Test quantité vide

    def test_quantite_none(self):

        with Session(test_engine) as session:

            with self.assertRaises(ValueError):

                ajout_order(
                    "commande1",
                    None,
                    1,
                    1,
                    session
                )


    # Test quantité qui n'est pas un entier

    def test_quantite_n_est_pas_un_entier(self):

        with Session(test_engine) as session:

            with self.assertRaises(ValueError):

                ajout_order(
                    "commande1",
                    "5",
                    1,
                    1,
                    session
                )


    # Test quantité inférieure ou égale à zéro

    def test_quantite_invalide(self):

        with Session(test_engine) as session:

            with self.assertRaises(ValueError):

                ajout_order(
                    "commande1",
                    0,
                    1,
                    1,
                    session
                )


    # Test utilisateur inexistant

    def test_user_inexistant(self):

        with Session(test_engine) as session:

            with self.assertRaises(ValueError):

                ajout_order(
                    "commande1",
                    5,
                    999999,
                    1,
                    session
                )


    # Test produit inexistant

    def test_product_inexistant(self):

        with Session(test_engine) as session:

            with self.assertRaises(ValueError):

                ajout_order(
                    "commande1",
                    5,
                    1,
                    999999,
                    session
                )


    # Test lecture de toutes les commandes

    def test_lire_orders(self):

        with Session(test_engine) as session:

            commandes = lire_order_service(session)

            self.assertIsNotNone(commandes)


    # Test lecture lorsque la base est vide

    def test_lire_orders_base_vide(self):

        with Session(test_engine) as session:

            session.query(Order).delete()
            session.commit()

            commandes = lire_order_service(session)

            self.assertEqual(
                commandes,
                []
            )


if __name__ == "__main__":
    unittest.main()