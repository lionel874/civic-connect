from sqlalchemy.orm import Session
from database import Base
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
                longitude="10.1",
                latitude="5.4"
            )

            session.add(user)
            session.add(location)
            session.commit()

            session.refresh(user)
            session.refresh(location)

            service = ajout_service(
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


if __name__ == "__main__":
    unittest.main()