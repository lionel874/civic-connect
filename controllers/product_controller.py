from CLASS.product import Product

class Product_controller:
    def __init__(self):
        self.products = []

    def ajouter_produit(self, product):
        self.products.append(product)

    def modif_product(self,id_p, new_nom, new_prix, new_quantite):
        for product in self.products :
            if id_p == id_p:
                nom_p.product = new_nom
                