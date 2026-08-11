from controllers.report_controller import ajout_report
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
        longitude = 10.25,
        latitude=5.45
    )

    with Session(test_engine) as session:

        session.add(user)
        session.add(localisation)

        session.commit()

        user_id = user.id
        location_id = localisation.id_l

    signalement = ajout_report(
        1,
        "titre",
        "description",
        user_id,
        location_id,
        test_engine
    )

    self.assertIsNotNone(signalement) 



if __name__ == " __main__":
    unittest.main()