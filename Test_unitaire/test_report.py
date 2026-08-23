from SERVICES.report_service import (
    ajout_report_service,
    identifier_report_service,
    lire_report_service,
    supprimer_report_service
)
from CLASS.report import Report
import unittest
from sqlalchemy import create_engine
from  database import Base
from CLASS.users import User
from CLASS.location import Location
from sqlalchemy.orm import Session

test_engine = create_engine(
    "sqlite:///test_database/test_civic_connect.db"
)
Base.metadata.create_all(test_engine)


class TestAjoutReport(unittest.TestCase):

    # test si tout est valide 

   def test_report_valide(self):

    user = User(
        nom="moudouthe",
        prenom="lionel",
        email="lionel@gmail.com",
        tel="680048703",
        role="admin"
    )

    localisation = Location(
        ville="dschang",
        quartier="tchouale",
        adresse="rue-456",
        
    )

    with Session(test_engine) as session:

        session.add(user)
        session.add(localisation)

        session.commit()

        user_id = user.id
        location_id = localisation.id_l

    signalement = ajout_report_service(
        1,
        "titre",
        "description",
        user_id,
        location_id,
        test_engine
    )

    self.assertIsNotNone(signalement) 




# test identification par id

    def test_identifier_report_par_id(self):

        with Session(test_engine) as session:

            user = User(
                nom="test",
                prenom="user",
                email="testreport@gmail.com",
                tel="680048704",
                role="user"
            )

            localisation = Location(
                ville="dschang",
                quartier="tchouale",
                adresse="rue-123"
            )

            session.add(user)
            session.add(localisation)

            session.commit()

            signalement = ajout_report_service(
                1,
                "Incident",
                "Probleme de connexion",
                user.id,
                localisation.id_l,
                session
            )

            report_id = signalement.id_r

            resultat = identifier_report_service(
                report_id,
                session
            )
  

# test identification report inexistant
   def test_identifier_report_inexistant(self):
  
          with Session(test_engine) as session:
  
              with self.assertRaises(ValueError):
  
                  identifier_report_service(
                      999,
                      session
                  )
  # test lire tous les report
    
   def test_lire_report(self):

        with Session(test_engine) as session:

            user = User(
                nom="lecture",
                prenom="test",
                email="lecture@gmail.com",
                tel="680048705",
                role="user"
            )

            localisation = Location(
                ville="dschang",
                quartier="tchouale",
                adresse="rue-789"
            )

            session.add(user)
            session.add(localisation)

            session.commit()

            report1 = ajout_report_service(
                
                "Report 1",
                "Description 1",
                user.id,
                localisation.id_l,
                session
            )

            report2 = ajout_report_service(
                
                "Report 2",
                "Description 2",
                user.id,
                localisation.id_l,
                session
            )

            reports = lire_report_service(session)

            self.assertIsNotNone(reports)
            self.assertIn(report1, reports)
            self.assertIn(report2, reports)
   def test_lire_reports_base_vide(self):

        with Session(test_engine) as session:

            session.query(Report).delete()
            session.commit()

            reports = lire_report_service(session)

            self.assertEqual(reports, [])

        def test_supprimer_report(self):

         with Session(test_engine) as session:

            user = User(
                nom="supprimer",
                prenom="test",
                email="supprimerreport@gmail.com",
                tel="680048707",
                role="user"
            )

            localisation = Location(
                ville="dschang",
                quartier="tchouale",
                adresse="rue-222"
            )

            session.add(user)
            session.add(localisation)

            session.commit()

            signalement = ajout_report_service(
                1,
                "Report à supprimer",
                "Description",
                user.id,
                localisation.id_l,
                session
            )

            report_id = signalement.id_r

            supprimer_report_service(
                report_id,
                session
            )

            resultat = session.get(
                Report,
                report_id
            )

            self.assertIsNone(resultat)
if __name__ == " __main__":
    unittest.main()