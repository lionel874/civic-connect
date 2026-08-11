from sqlalchemy.orm import Session
from database import engine,Base
from CLASS.product import Product
from controllers.product_controller import ajoute_p
from sqlalchemy import create_engine
import unittest

test_engine = create_engine(
    "sqlite:///test_database/test_civic_connect.db"
)
Base.metadata.create_all(test_engine)

class TestAjoutProduit(unittest.TestCase):

    # ajout en condition normal

    def test_ajout_valide(self):
        
        produit = ajoute_p("produit-1",
                           "1000 fcfa",
                           "10 article",
                           test_engine)
        self.assertIsNotNone(produit)

    # ajout lorsque parametre nom produit est vide
    
    def  test_nom_vide(self):
        with self.assertRaises(ValueError):
            ajoute_p("",
                    "1000 fcfa",
                    "10 article",
                    test_engine)
            
    #ajout lorsque parametre prix produit est vide

    def  test_prix_vide(self):
            with self.assertRaises(ValueError):
                ajoute_p("produit-1",
                        "",
                        "10 article",
                        test_engine)


    #ajout lorsque parametre quantite produit est vide
    
    def test_ajout_valide(self):
        with self.assertRaises(ValueError):
             ajoute_p("produit-1",
                               "1000 fcfa",
                               "",
                               test_engine)


    ####### les tests pour verifier le format

    # test pour verifier si nom n'est pas un str

    def test_nom_pas_str(self):
         with self.assertRaises(ValueError):
              ajoute_p(123,
                       "1000 fcfa",
                       "10 articles",
                       test_engine)
    
   # test pour verifier si prix n'est pas un str

    def test_prix_pas_str(self):
         with self.assertRaises(ValueError):
              ajoute_p("produit-1",
                       123,
                       "10 articles",
                       test_engine)

    # test pour verifier si quantite n'est pas un str

    def test_prix_pas_str(self):
             with self.assertRaises(ValueError):
                  ajoute_p("produit-1",
                           "1000 fcfa",
                           123,
                           test_engine)


    # test lorsque le parametre nom est none

    def test_nom_none(self):
    
          with self.assertRaises(ValueError):
               ajoute_p(None,
                        "1000 fcfa",
                        "10 articles",
                         test_engine
                        
                    
               )   

if __name__ == "__main__":
    unittest.main() 
    

    
