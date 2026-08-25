from CLASS.report import Report
from database import SessionLocal



# creation d'1 signalement dans la bd

def create_report_repository(signalement):

    db = SessionLocal()

    try:
        db.add(signalement)
        db.commit()
        db.refresh(signalement)

        return signalement

    finally:
        db.close()


# Lire tous les signalements
def lire_report_repository():

    db = SessionLocal()

    try:
        return db.query(Report).all()

    finally:
        db.close()


# Identifier un signalement par ID
def identifier_report_par_id(report_id: int):

    db = SessionLocal()

    try:
        report = db.get(Report, report_id)

        return report

    finally:
        db.close()


# Modifier un signalement
def modifier_report_repository(
    report_id: int,
    titre,
    description,
    
):

    db = SessionLocal()

    try:

        report = db.get(Report, report_id)

        if report is None:
            return None

        report.titre = titre
        report.description = description
        
        db.commit()
        db.refresh(report)

        return report

    finally:
        db.close()


# Supprimer un signalement par ID
def supprimer_report_repository(report_id: int):

    db = SessionLocal()

    try:

        report = db.get(Report, report_id)

        if report is None:
            return None

        db.delete(report)
        db.commit()

        return report

    finally:
        db.close()