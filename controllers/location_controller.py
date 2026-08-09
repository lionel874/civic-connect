from sqlalchemy.orm import Session
from CLASS.location import Location
from database import engine

def ajout_localisation( ville, quartier, adresse):
    with Session(engine) as session:
        localisation = Location(
                                ville = ville,
                                quartier = quartier,
                                adresse = adresse)

        session.add(localisation)
        session.commit()