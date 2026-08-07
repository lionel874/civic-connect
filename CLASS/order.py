class Order:
    def __init__(self,num_order, nom_order,quantite,montant_total,user_id,product_id,statut):
        self.num_order = num_order
        self.nom_order = nom_order
        self.quantite = quantite
        self.montant_total = montant_total
        self.user_id = user_id
        self.product_id = product_id
        self.statut = statut

    def afiichage_order(self):
        print("numero_commander :",self.num_order,"nom_commande :",self.nom_order,
              "quantite", self.quantite,"montant :", self.montant_total , "id_user :",self.user_id,"id_produit :",self.product_id, "statut_cmd :",self.statut)
    def modifier_nom_order(self,new_nom_order):
        self.num_order = new_nom_order
    def modifier_quantite(self,new_quantite):
        self.quantite = new_quantite
    def modifier_montant(self,new_montant):
        self.montant_total = new_montant
    def modif_status(self,new_statut):
        self.statut = new_statut