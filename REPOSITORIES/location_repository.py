from sqlalchemy.orm import Session
from CLASS.location import Location

# creation d'une location dans la base donnee

def create_location_repository(localisation:Location, session:Session):
    
        session.add(localisation)
        session.commit()
        session.refresh(localisation)
        return localisation 