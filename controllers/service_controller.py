from sqlalchemy.orm import Session
from CLASS.service import Service
from database import engine

def ajout_service( nom_service, description, prix, user_id, localisation_id):
    with Session(engine) as session :
        servic= Service(
                        nom_s = nom_service,
                        description = description,
                        prix = prix,
                         user_id = user_id,
                         location_id = localisation_id)
        session.add(servic)
        session.commit()
        