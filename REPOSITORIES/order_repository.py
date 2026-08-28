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

# Identifier une commande par ID
def identifier_order_par_id(order_id: int):

    db = SessionLocal()

    try:
        order = db.get(Order, order_id)

        return order

    finally:
        db.close()


# Modifier une commande (PUT - remplacement complet)
def modifier_order_repository(
    order_id: int,
    titre,
    quantite,
    mte_total,
    product_id
):

    db = SessionLocal()

    try:
        order = db.get(Order, order_id)

        if order is None:
            return None

        order.titre_o = titre
        order.quantite_o = quantite
        order.mte_total = mte_total
        order.product_id = product_id

        db.commit()
        db.refresh(order)

        return order

    finally:
        db.close()


# Modifier partiellement une commande (PATCH)
def patch_order_repository(
    order_id: int,
    titre=None,
    quantite=None,
    mte_total=None,
    product_id=None
):

    db = SessionLocal()

    try:
        order = db.get(Order, order_id)

        if order is None:
            return None

        if titre is not None:
            order.titre_o = titre

        if quantite is not None:
            order.quantite_o = quantite

        if mte_total is not None:
            order.mte_total = mte_total

        if product_id is not None:
            order.product_id = product_id

        db.commit()
        db.refresh(order)

        return order

    finally:
        db.close()


# Supprimer une commande par ID
def supprimer_order_repository(order_id: int):

    db = SessionLocal()

    try:
        order = db.get(Order, order_id)

        if order is None:
            return None

        db.delete(order)
        db.commit()

        return order

    finally:
        db.close()