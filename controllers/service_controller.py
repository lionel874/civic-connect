from sqlalchemy.orm import Session
from CLASS.service import Service
from database import engine

def ajout_service(nom, description,prix, user_id,location_id, db_engine=engine):
    with Session(db_engine) as session:

        service = Service(
            nom_s=nom,
            description=description,
            prix =prix,
            user_id=user_id,
            location_id = location_id
        )

        session.add(service)
        session.commit()
        session.refresh(service)

        return service
        