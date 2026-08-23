from sqlalchemy.orm import Session
from database import Base
from CLASS.location import Location
from SERVICES.location_service import(ajout_localisation_service,lire_localisation_service)
import unittest
from sqlalchemy import create_engine

test_engine = create_engine(
    "sqlite:///test_database/test_civic_connect.db"
)
Base.metadata.create_all(test_engine)


class TestAjoutLocation(unittest.TestCase):
    # test ajout de localisation valide 
    def test_ajout_location_valide(self):
        with Session(test_engine) as session: 
          localisation = ajout_localisation_service("dschang",
                                          "tchouale",
                                          "rue-456",
                                          
                                          session)
        self.assertIsNotNone(localisation)

    # test lorsque le parametre ville est vide
    def test_ville_vide(self):
        with self.assertRaises(ValueError):
            ajout_localisation_service("",
                               "tchouale",
                               "rue-456",
                               
                               test_engine)
    # test lorsque le parametre quartier est vide
    def test_quartier_vide(self):
        with self.assertRaises(ValueError):
            ajout_localisation_service("dschang",
                               "",
                               "rue-456",
                               test_engine)

    # test lorsque le parametre adresse est vide

    def test_adresse_vide(self):
        with self.assertRaises(ValueError):
            ajout_localisation_service("dscchang",
                               "tchouale",
                               "",
                               test_engine)

     

  
   # test de verification de format

    def test_ville_pas_str(self):
        with self.assertRaises(ValueError):
            ajout_localisation_service(123,"tchouale",
                                   "rue-456",
                                   
                                   test_engine)     

    #### quartier est un str
    def test_quartier_pas_str(self):
            with self.assertRaises(ValueError):
                ajout_localisation_service("dschang",123,
                                       "rue-456",
                                       
                                       test_engine) 
    ## adresse str
    def test_adresse_pas_str(self):
            with self.assertRaises(ValueError):
                ajout_localisation_service("dschang","tchouale",
                                       123,
                                       
                                       test_engine) 
    
      
    # test si ville == none

    def test_ville_none(self):
        with self.assertRaises(ValueError):
            ajout_localisation_service(None,
                               "tchouale",
                               "rue-456",
                               
                               test_engine)

    


    # test pour lire les localisation

    def lire_localisation(self):
         with Session(test_engine) as session:
              localisation1 = Location(
                   ville ="yaounde",
                   quartier ="bastos",
                   adresse ="rue-10"
                   
              )
              localisation2 = Location(
                                 ville ="douala",
                                 quartier ="makepe",
                                 adresse ="rue 13"
                                 
                            )

              session.add_all([localisation1,
                             localisation2])

              session.commit()

    def test_lire_localisation_base_vide(self):
    
            with Session(test_engine) as session:
    
                # On supprime les utilisateurs présents
                session.query(Location).delete()
                session.commit()
    
                localisation = lire_localisation_service(session)
    
                self.assertEqual(
                    localisation,
                    []
                ) 
    
if __name__ == "__main__":
     unittest.main()