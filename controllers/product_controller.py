from sqlalchemy.orm import Session
from CLASS.product import Product
from database import engine

def ajoute_p(nom, prix, quantite):
    with Session(engine) as session:
        produit = Product(nom_p=nom,
                          prix_p = prix,
                          quantite_p = quantite)

        session.add(produit)
        session.commit()

        print("produit ajoute")

def modifier_produit(produit_id, nouveau_prix,nouvelle_qte):
    with Session(engine) as session:
        produit = session.get(Product,produit_id)
        if produit is None:
            print("produit introuvable")
            return
        produit.prix_p = nouveau_prix
        produit.quantite_p = nouvelle_qte

        session.commit()