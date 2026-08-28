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
def lire_report_repository(type: str = None, 
                           statut: str = None, 
                           page: int = 1, 
                           limit: int = 10):
    db = SessionLocal()
    try:
        query = db.query(Report)

        if type:
            query = query.filter(Report.type == type)

        if statut:
            query = query.filter(Report.statut == statut)

        query = query.order_by(Report.date.desc())

        total = query.count()
        resultats = query.offset((page - 1) * limit).limit(limit).all()

        return {
            "total": total,
            "page": page,
            "limit": limit,
            "resultats": resultats
        }
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