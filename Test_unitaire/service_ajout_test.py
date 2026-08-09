from sqlalchemy.orm import Session
from database import engine,Base
from CLASS.service import Service
from CLASS.users import User
from CLASS.location import Location
from controllers.service_controller import ajout_service

ajout_service("service-1",
              "description",
              "40.000fcfa",
              1,1)
with Session(engine) as session:
    service=  session.query(Service).filter_by(nom_s = "service-1").first()
    assert service is not None
    assert service.nom_s =="service-1"
    assert service.description =="description"
    assert service.prix == "40.000fcfa"
    assert service.user_id ==1
    assert service.location_id ==1