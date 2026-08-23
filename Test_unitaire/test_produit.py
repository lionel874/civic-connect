from sqlalchemy.orm import Session
from database import engine,Base
from CLASS.product import Product
from SERVICES.product_service import (lire_products_service,
                                      ajout_produit_service,
                                      modif_produit_service,
                                      supprimer_product_service)
from sqlalchemy import create_engine
import unittest

test_engine = create_engine(
    "sqlite:///test_database/test_civic_connect.db"
)
Base.metadata.create_all(test_engine)

class TestAjoutProduit(unittest.TestCase):

    # ajout en condition normal

    def test_ajout_valide(self):
        
        produit = ajout_produit_service("produit-1",
                           "1000 fcfa",
                           "10 article",
                           test_engine)
        self.assertIsNotNone(produit)

    # ajout lorsque parametre nom produit est vide
    
    def  test_nom_vide(self):
        with self.assertRaises(ValueError):
            ajout_produit_service("",
                    "1000 fcfa",
                    "10 article",
                    test_engine)
            
    #ajout lorsque parametre prix produit est vide

    def  test_prix_vide(self):
            with self.assertRaises(ValueError):
                ajout_produit_service("produit-1",
                        "",
                        "10 article",
                        test_engine)


    #ajout lorsque parametre quantite produit est vide
    
    def test_ajout_valide(self):
        with self.assertRaises(ValueError):
             ajout_produit_service("produit-1",
                               "1000 fcfa",
                               "",
                               test_engine)


    ####### les tests pour verifier le format

    # test pour verifier si nom n'est pas un str

    def test_nom_pas_str(self):
         with self.assertRaises(ValueError):
              ajout_produit_service(123,
                       "1000 fcfa",
                       "10 articles",
                       test_engine)
    
   # test pour verifier si prix n'est pas un str

    def test_prix_pas_str(self):
         with self.assertRaises(ValueError):
              ajout_produit_service("produit-1",
                       123,
                       "10 articles",
                       test_engine)

    # test pour verifier si quantite n'est pas un str

    def test_prix_pas_str(self):
             with self.assertRaises(ValueError):
                  ajout_produit_service("produit-1",
                           "1000 fcfa",
                           123,
                           test_engine)


    # test lorsque le parametre nom est none

    def test_nom_none(self):
    
          with self.assertRaises(ValueError):
               ajout_produit_service(None,
                        "1000 fcfa",
                        "10 articles",
                         test_engine
                        
                    
               )  
# test pour lire tout les produit

    def test_lire_produit(self):
         with Session(test_engine) as session:
              produit1= Product(nom_p="pc1",
                                prix_p=12.500,
                                quantite_p= 5)
              produit2 = Product(nom_p="pc2",
                                 prix_p=13.546,
                                 quantite_p=3)
              session.add_all([produit1,produit2])
              session.commit()



    def test_lire_produit_base_vide(self):
   
           with Session(test_engine) as session:
   
               # On supprime les utilisateurs présents
               session.query(Product).delete()
               session.commit()
   
               produit = lire_products_service(session)
   
               self.assertEqual(
                   produit,
                   []
               ) 

    # supprimer un produit
    def test_supprimer_produit(self):
    
            with Session(test_engine) as session:
    
                produit = Product(
                    nom_p="p1",
                    prix_p=12.500,
                    quantite_p=7
                )
    
                session.add(produit)
    
                session.commit()
    
                session.refresh(produit)
    
                produit_id = produit.id
    
                supprimer_product_service(
                    produit_id,
                    session
                )
    
                produit_supprime = session.get(
                    Product,
                    produit_id
                )
    
                self.assertIsNone(
                    produit_supprime
                )
    
    
    def test_supprimer_produit_inexistant(self):
    
            with Session(test_engine) as session:
    
                with self.assertRaises(ValueError):
    
                    supprimer_product_service(
                        99,
                        session
                    )
    

if __name__ == "__main__":
    unittest.main() 
    

    
