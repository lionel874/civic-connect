from database import SessionLocal
from CLASS.service import Service
from CLASS.users import User
from CLASS.location import Location
from sqlalchemy import or_
# creation d'un service dans la base de donnee

def create_service(service):
    
        
    db =SessionLocal()
    try:
     db.add(service)
     db.commit()
     db.refresh(service)
     return service
    finally:
        db.close()


def lire_service_repository(categorie: str = None, mot_cle: str = None, zone: str = None, page: int = 1, limit: int = 10):
    db = SessionLocal()
    try:
        query = db.query(Service).join(Location, Service.location_id == Location.id_l)

        conditions = []

        if categorie:
            conditions.append(Service.categorie == categorie)

        if mot_cle:
            conditions.append(Service.nom_s.contains(mot_cle))

        if zone:
            conditions.append(Location.ville.contains(zone))
            conditions.append(Location.quartier.contains(zone))
        if conditions:
            query = query.filter(or_(*conditions))

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

def verifier_user_repository(user_id):

    db = SessionLocal()

    try:
        return db.get(User, user_id)

    finally:
        db.close()


def identifier_service_par_id(service_id:int ): 
      db =SessionLocal()
      try:
        service = db.get(Service,service_id)

        return service
      finally:
          db.close


def supprimer_service_repository(service_id):
    db = SessionLocal()
        
    
    try:

        service = db.query(Service).filter(
            Service.id_s == service_id
        ).first()

        if service_id is None:
            return None

        db.delete(service)
        db.commit()

        return {
            "message": "service supprimé avec succès"
        }

    finally:
        db.close()