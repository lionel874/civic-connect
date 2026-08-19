from sqlalchemy.orm import Session
from CLASS.service import Service

# creation d'un service dans la base de donnee

def create_service(service: Service, session:Session):
    
        session.add(service)
        session.commit()
        session.refresh(service)
        return service
