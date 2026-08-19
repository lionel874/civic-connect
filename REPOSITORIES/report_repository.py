from CLASS.report import Report
from sqlalchemy.orm import Session
from CLASS.location import Location
from CLASS.users import User


# creation d'1 signalement dans la bd

def create_report_repository(signalement: Report,
    session: Session):
    
        session.add(signalement)
        session.commit ()
        session.refresh(signalement)
        return signalement