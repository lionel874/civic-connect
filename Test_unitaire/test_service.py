from sqlalchemy.orm import Session
from database import engine,Base
from CLASS.service import Service
from CLASS.users import User
from CLASS.location import Location
from controllers.service_controller import ajout_service
import unittest
from sqlalchemy import create_engine
test_engine = create_engine(
    "sqlite:///test_database/test_civic_connect.db"
)
Base.metadata.create_all(test_engine)

class TestAjoutService(unittest.TestCase):
     def test_service_valide(self):

    # Créer un utilisateur
      user = User(
        nom="moudouthe",
        prenom="lionel",
        email="lionel@gmail.com",
        tel="680048703",
        role="admin"
    )
     with Session(test_engine) as session: session.add(user) 
     session.commit()  
     with self.assertRaises(ValueError): 
        ajout_service( "service-1",
                       "", 
                         test_engine ) 
      
if __name__ == "__main__": 
   unittest.main()   

