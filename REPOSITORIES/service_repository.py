from database import SessionLocal
from CLASS.service import Service
from CLASS.users import User

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


def lire_service_repository():
            db = SessionLocal()
            try:
             return db.query(Service).all()
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