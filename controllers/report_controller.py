from sqlalchemy.orm import Session
from CLASS.report import Report
from database import engine

def ajout_report(id_r, titre, description, user_id, location_id):
    with Session(engine) as session :
        signalment = Report( report_id = id_r,
                            titre_report = titre,
                            descrpt_report = description,
                            user = user_id,
                            location_report = location_id)

        session.add(signalment)
        session.commit()