from sqlalchemy.orm import Session
from CLASS.service import Service
from database import engine

def ajout_service(nom, description, user_id, db_engine=engine):
    with Session(db_engine) as session:

        service = Service(
            nom_s=nom,
            description_s=description,
            user_id=user_id
        )

        session.add(service)
        session.commit()

        return service
        