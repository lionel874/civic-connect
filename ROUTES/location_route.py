from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from SERVICES.location_service import ajout_localisation_service,lire_localisation_service


router = APIRouter(
    prefix= "/localisation",
    tags=["Location"]
)

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()


@router.post("/")

def create_location(ville: str,
                    quartier:str,
                    adresse: str,
                    session: Session = Depends(get_db)):
    return ajout_localisation_service(ville, quartier, adresse, session)