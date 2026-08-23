from sqlalchemy.orm import Session
import unittest
from database import Base
from CLASS.users import User
from sqlalchemy import create_engine
from SERVICES.user_service import (ajout_user,
                                   lire_users_service,
                                   supprimer_user_service)

test_engine = create_engine(
    "sqlite:///test_database/test_civic_connect.db"
)
Base.metadata.create_all(test_engine)



class TestUserService(unittest.TestCase):
    
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



    # test pour lire tous les utilisateur

    def test_lire_users(self):

        with Session(test_engine) as session:

            user1 = User(
                nom="User1",
                prenom="Test",
                email="user1@gmail.com",
                tel="680000001",
                role="user"
            )

            user2 = User(
                nom="User2",
                prenom="Test",
                email="user2@gmail.com",
                tel="680000002",
                role="admin"
            )

            session.add_all([
                user1,
                user2
            ])

            session.commit()

            utilisateurs = lire_users_service(session)

            self.assertIsNotNone(utilisateurs)

            self.assertIn(user1, utilisateurs)

            self.assertIn(user2, utilisateurs)


    def test_lire_users_base_vide(self):

        with Session(test_engine) as session:

            # On supprime les utilisateurs présents
            session.query(User).delete()
            session.commit()

            utilisateurs = lire_users_service(session)

            self.assertEqual(
                utilisateurs,
                []
            ) 



# test supprimer user
    def test_supprimer_user(self):

        with Session(test_engine) as session:

            utilisateur = User(
                nom="u1",
                prenom="pp",
                email="u1@gmail.com",
                tel="680000003",
                role="user"
            )

            session.add(utilisateur)

            session.commit()

            session.refresh(utilisateur)

            user_id = utilisateur.id

            supprimer_user_service(
                user_id,
                session
            )

            utilisateur_supprime = session.get(
                User,
                user_id
            )

            self.assertIsNone(
                utilisateur_supprime
            )


    def test_supprimer_user_inexistant(self):

        with Session(test_engine) as session:

            with self.assertRaises(ValueError):

                supprimer_user_service(
                    999999,
                    session
                )


if __name__ == "__main__":
    unittest.main()