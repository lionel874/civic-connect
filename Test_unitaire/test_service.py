from sqlalchemy.orm import Session
from database import Base
from CLASS.users import User
from CLASS.location import Location
from SERVICES.services_service import lire_service_service,ajout_service
import unittest
from sqlalchemy import create_engine


test_engine = create_engine(
    "sqlite:///test_database/test_civic_connect.db"
)

Base.metadata.create_all(test_engine)


class TestAjoutService(unittest.TestCase):

    def test_service_valide(self):

        with Session(test_engine) as session:

            user = User(
                nom="moudouthe",
                prenom="lionel",
                email="lionel_service@gmail.com",
                tel="680048704",
                role="admin"
            )

            location = Location(
                ville="Dschang",
                quartier="Centre",
                adresse="Rue 1",
                
            )

            session.add(user)
            session.add(location)
            session.commit()

            session.refresh(user)
            session.refresh(location)

            service = (
                "service-1",
                "internet haut debit",
                "5000",
                user.id,
                location.id_l,
                test_engine
            )

            self.assertEqual(service.nom_s, "service-1")
            self.assertEqual(
                service.description,
                "internet haut debit")



    def test_lire_services(self):

     with Session(test_engine) as session:

        service = ajout_service(
            nom_s="service-1",
            description="description",
            prix=100
        )

        session.add(service)
        session.commit()

        services = lire_service_service(session)

        self.assertIsInstance(services, list)
        self.assertGreater(len(services), 0)


    # lire les tous service

    def test_lire_services(self):

     with Session(test_engine) as session:

        user = User(
            nom="moudouthe",
            prenom="lionel",
            email="lecture_service@gmail.com",
            tel="680048703",
            role="admin"
        )

        localisation = Location(
            ville="dschang",
            quartier="tchouale",
            adresse="rue-456"
        )

        session.add(user)
        session.add(localisation)
        session.commit()

        service = ajout_service(
            "service-1",
            "description service",
            100,
            user.id,
            localisation.id_l,
            session
        )

        services = lire_service_service(session)

        self.assertIsInstance(services, list)
        self.assertGreater(len(services), 0)
        self.assertIn(service, services)

if __name__ == "__main__":
    unittest.main()