from database import SessionLocal
from CLASS.location import Location

# creation d'une location dans la base donnee

def create_location_repository(localisation):
        db =SessionLocal()
        try:
         db.add(localisation)
         db.commit()
         db.refresh(localisation)
         return localisation
        finally:
            db.close()

def lire_localisation_repository():
            db = SessionLocal()
            try:
             return db.query(Location).all()
            finally:
                db.close()

def identifier_localisation_par_id(location_id:int): 
      db =SessionLocal()
      try:
        localisation = db.query(Location).filter(
            Location.id_l == location_id
        ).first()


        return localisation
      finally:
          db.close

def supprimer_localisation_repository(location_id:int):
    db = SessionLocal()
        
    
    try:

        localisation = db.query(Location).filter(
            Location.id_l == location_id
        ).first()

        if localisation is None:
            return None

        db.delete(localisation)
        db.commit()

        return {
            "message": "localisation supprimé avec succès"
        }

    finally:
        db.close()
