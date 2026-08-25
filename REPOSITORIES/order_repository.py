from database import SessionLocal
from CLASS.order import Order

# creation d'une commande dans la base de donnee

def create_order_repo(commande):
            
            db = SessionLocal()
        
            try:
                db.add(commande)
                db.commit()
                db.refresh(commande)
        
                return commande
        
            finally:
                db.close()

def lire_order_repository():

    db = SessionLocal()

    try:
        return db.query(Order).all()

    finally:
        db.close()
