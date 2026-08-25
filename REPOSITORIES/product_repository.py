from database import SessionLocal
from CLASS.product import Product

# creation 1 produit dans la bd

def create_product_repo(produit):

            db =SessionLocal()
            try:
             db.add(produit)
             db.commit()
             db.refresh(produit)
             return produit
            finally:
                db.close()

# modification de produit dans la bd

def modif_produit_repo(
    product_id,
    nom_p,
    prix_p,
    quantite_p
):

    db = SessionLocal()

    try:

        produit = db.query(Product).filter(
            Product.id_p == product_id
        ).first()

        if produit is None:
            return None

        produit.nom_p = nom_p
        produit.prix_p = prix_p
        produit.quantite_p = quantite_p

        db.commit()
        db.refresh(produit)

        return produit

    finally:
        db.close()


def identifier_produit_par_id(product_id: int):

    db = SessionLocal()

    try:
        produit = db.query(Product).filter(
            Product.id_p == product_id
        ).first()

        return produit

    finally:
        db.close()

# Supprimer un produit par son ID
def supprimer_produit_repository(product_id: int):

    db = SessionLocal()

    try:

        produit = db.query(Product).filter(
            Product.id_p == product_id
        ).first()

        if produit is None:
            return None

        db.delete(produit)
        db.commit()

        return {
            "message": "Produit supprimé avec succès"
        }

    finally:
        db.close()


def lire_produit_repository():

    db = SessionLocal()

    try:
        produits = db.query(Product).all()

        return produits

    finally:
        db.close()


def patch_product_repository(
    product_id,
    nom_p=None,
    prix_p=None,
    quantite_p=None,
    
):
    db = SessionLocal()

    try:
        produit = db.query(Product).filter(
            Product.id_p== product_id
        ).first()

        if produit is None:
            return None

        if nom_p is not None:
            produit.nom_p = nom_p

        if prix_p is not None:
            produit.prix_p = prix_p

        if quantite_p is not None:
            produit.quantite_p = quantite_p

        

        db.commit()
        db.refresh(produit)

        return produit

    finally:
        db.close()