from sqlalchemy.orm import Session
from database import engine,Base
from CLASS.product import Product
from controllers.product_controller import ajoute_p

ajoute_p("pc",
         "12.000 fcfa",
         "25 article")
#verification a la base
with Session(engine) as session :
    produit = session.query(Product).filter_by(nom_p = "pc").first()
    assert produit is not None
    assert produit.nom_p =="pc"
    assert produit.prix_p =="12.000 fcfa"
    assert produit.quantite_p =="25 article"