from CLASS.report import Report
from sqlalchemy.orm import Session



# creation d'1 signalement dans la bd

def create_report_repository(signalement: Report,
    session: Session):
    
        session.add(signalement)
        session.commit ()
        session.refresh(signalement)
        return signalement

def lire_report_repository(session: Session):
      return session.query(Report).all()

def identifier_report_par_id(report_id: int, session: Session):

    report = session.get(Report, report_id)

    return report
def supprimer_report_repository(
    report_id: int,
    session: Session
):

    report = session.get(Report, report_id)

    if report is None:
        return None

    session.delete(report)
    session.commit()

    return report
