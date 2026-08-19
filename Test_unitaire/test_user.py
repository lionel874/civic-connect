from sqlalchemy.orm import Session
import unittest
from database import Base, engine
from CLASS.users import User
from controllers.user_controller import ajout_user
from sqlalchemy import create_engine

test_engine = create_engine(
    "sqlite:///test_database/test_civic_connect.db"
)
Base.metadata.create_all(test_engine)



class TestAjoutUser(unittest.TestCase):
    
# user ajouter normalement

    def test_ajout_user_valide(self):
       with Session(test_engine) as session: 
        utilisateur = ajout_user("moudouthe",
                          "lionel",
                          "lionel@gmail.com",
                          "680048703",
                          "admin", session)
        self.assertIsNotNone(utilisateur)
        
# test lorsque le parametre nom est vide
    def test_nom_vide(self):
      with Session(test_engine) as session:
        with self.assertRaises(ValueError):
            ajout_user("",
                       "lionel",
                       "lionel@gmail.com",
                       "680048703",
                       "admin",session)
            
# test lorsque le parametre prenom est vide

    def test_prenom_vide(self):
     with Session(test_engine) as session:
        with self.assertRaises(ValueError):
            ajout_user("moudouthe",
                        "",
                        "lionel@gmail.com",
                        "680048703",
                        "admin",session)

# test lorsque le parametre email est vide

    def test_email_vide(self):
         with Session(test_engine) as session:
            with self.assertRaises(ValueError):
                 ajout_user("moudouthe",
                             "lionel",
                             "",
                             "680048703",
                             "admin",session)

# test lorsque le parametre numero de telephone est vide

    def test_tel_vide(self):
        with Session(test_engine) as session:
            with self.assertRaises(ValueError):
                 ajout_user("moudouthe",
                             "lionel",
                             "lionel@gmail.com",
                             "",
                             "admin",session)




# test lorsque le parametre nom est none

    def test_nom_none(self):
     with Session(test_engine) as session:
       with self.assertRaises(ValueError):
        ajout_user(
            None,
            "Lionel",
            "lionel@gmail.com",
            "680048703",
            "admin",session
        )

# test de verication de format

    def test_nom_n_est_pas_une_chaine(self):
      with Session(test_engine) as session: 
        with self.assertRaises(ValueError):
          ajout_user(
            123,
            "Lionel",
            "lionel@gmail.com",
            "680048703",
            "admin",
            session
        )


# test le numero doit commencer par 6
   
    def test_tel_doit_commencer_par_6(self):
      with Session(test_engine) as session:
        with self.assertRaises(ValueError):
         ajout_user(
            "Moudouthe",
            "Lionel",
            "lionel@gmail.com",
            "580048703",
            "user",
            session
        )


# test le numero doit avoir uniqument des chiffre



    def test_tel_doit_contenir_uniquement_des_chiffres(self):
     with Session(test_engine) as session:
      with self.assertRaises(ValueError):
        ajout_user(
            "Moudouthe",
            "Lionel",
            "lionel@gmail.com",
            "68004ABC",
            "user",
            session
        )

 

 



    




# test email inavalide

    def test_email_invalide(self):
     with Session(test_engine) as session:
      with self.assertRaises(ValueError):
        ajout_user(
            "Moudouthe",
            "Lionel",
            "lionel@gmail",
            "680048703",
            "user",
            session
        )


# test email valide 

    def test_email_valide(self):
     with Session(test_engine) as session:
      user = ajout_user(
        "Moudouthe",
        "Lionel",
        "lionel@gmail.com",
        "680048703",
        "user",
        session
    )

     self.assertEqual(user.email, "lionel@gmail.com")

#test de verication des donnees dans la base de donnee

   
   
    def test_verifier_base_test(self):

     with Session(test_engine) as session:
        utilisateurs = session.query(User).all()

        print(utilisateurs)

        self.assertGreater(len(utilisateurs), 0)

if __name__ == "__main__":
    unittest.main()