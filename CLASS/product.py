class Product:
    def __init__(self,id_p,nom_p,prix_p,quantite_p):
        self.id_p =id_p
        self.nom_p = nom_p
        self.prix_p = prix_p
        self.quantite_p = quantite_p

    def affichage_product(self):
        print("identifiant_produit :",self.id_p ,"nom_produit:",self.nom_p, "prix :",self.prix,
              "quantite :",self.quantite_p)