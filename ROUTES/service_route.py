from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from SERVICES.services_service import ajout_service


router = APIRouter(
    prefix= "/service",
    tags=["Service"]
)


def get_db():
    db = SessionLocal()
    try :
        yield db
    finally:
        db.close()


@router.post("/")


def create_service_route(nom_s:str,
                   description:str,
                   prix: float,
                   user_id: int,
                   location_id: int,
                   db: Session = Depends(get_db)):
    return ajout_service(
        nom_s,
        description,
        prix,
        user_id,
        location_id,
        db
    )