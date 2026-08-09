from sqlalchemy.orm import Session
from database import engine,Base
from CLASS.location import Location
from controllers.location_controller import ajout_localisation

ajout_localisation("dschang",
                   "foto",
                   "rue 123")

# verification dans la base
with Session(engine) as session:
    localisation = session.query(Location).filter_by(ville ="dschang").first()
    assert localisation is not None
    assert localisation.ville =="dschang"
    assert localisation.quartier == "foto"
    assert localisation.adresse =="rue 123 "