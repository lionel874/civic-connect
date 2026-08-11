from sqlalchemy.orm import Session
from database import engine,Base
from CLASS.location import Location
from controllers.location_controller import ajout_localisation
import unittest
from sqlalchemy import create_engine

test_engine = create_engine(
    "sqlite:///test_database/test_civic_connect.db"
)
Base.metadata.create_all(test_engine)


class TestAjoutLocation(unittest.TestCase):
    # test ajout de localisation valide 
    def test_ajout_location_valide(self):
        localisation = ajout_localisation("dschang",
                                          "tchouale",
                                          "rue-456",
                                          "10.457","56.754",
                                          test_engine)
        self.assertIsNotNone(localisation)

    # test lorsque le parametre ville est vide
    def test_ville_vide(self):
        with self.assertRaises(ValueError):
            ajout_localisation("",
                               "tchouale",
                               "rue-456",
                               "10.457","56.754",
                               test_engine)
    # test lorsque le parametre quartier est vide
    def test_quartier_vide(self):
        with self.assertRaises(ValueError):
            ajout_localisation("dschang",
                               "",
                               "rue-456","10.457","56.754",
                               test_engine)

    # test lorsque le parametre adresse est vide

    def test_adresse_vide(self):
        with self.assertRaises(ValueError):
            ajout_localisation("dscchang",
                               "tchouale",
                               "","10.457","56.754",
                               test_engine)

    # test longitude vide
    def test_longitude_vide(self):
        with self.assertRaises(ValueError):
            ajout_localisation(
                              "dscchang",
                               "tchouale",
                               "rue-456",
                               "",
                               "56.754",
                               test_engine)

    
    # test latitude vide
    def test_latitude_vide(self):
            with self.assertRaises(ValueError):
                ajout_localisation(
                                  "dscchang",
                                   "tchouale",
                                   "rue-456",
                                   "10.457",
                                   "",
                                   test_engine) 

  
   # test de verification de format

    def test_ville_pas_str(self):
        with self.assertRaises(ValueError):
            ajout_localisation(123,"tchouale",
                                   "rue-456",
                                   "10.457","56.754",
                                   test_engine)     

    #### quartier est un str
    def test_quartier_pas_str(self):
            with self.assertRaises(ValueError):
                ajout_localisation("dschang",123,
                                       "rue-456",
                                       "10.457","56.754",
                                       test_engine) 
    ## adresse str
    def test_adresse_pas_str(self):
            with self.assertRaises(ValueError):
                ajout_localisation("dschang","tchouale",
                                       123,
                                       "10.457","56.754",
                                       test_engine) 
    ## longitude 
    def test_longitude_pas_str(self):
            with self.assertRaises(ValueError):
                ajout_localisation("dschang","tchouale",
                                       "rue-456",
                                       123,"56.754",
                                       test_engine)
    # latitude 
    def test_latitude_pas_str(self):
            with self.assertRaises(ValueError):
                ajout_localisation(123,"tchouale",
                                       "rue-456",
                                       "10.457",123,
                                       test_engine)    
      
    # test si ville == none

    def test_ville_none(self):
        with self.assertRaises(ValueError):
            ajout_localisation(None,
                               "tchouale",
                               "rue-456",
                               "10.457","56.754",
                               test_engine)

if __name__ == "__main__":
     unittest.main()