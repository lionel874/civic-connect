class User:
    def __init__(self,id_u,nom,prenom,email,tel,role):
        self.id_u = id_u
        self.nom =nom
        self.prenom =prenom
        self.email = email
        self.tel = tel
        self.role = role

    def afficher(self):
        print("id :", self.id_u, "nom :" , self.nom ,"prenom :",self.prenom , "email :", self.email,
              "tel:", self.tel,
              "role :", self.role)

    def modifier_nom_user(self, new_nom):
        self.nom = new_nom
    def modifier_nom_prenom(self,new_prenom):
        self.prenom =new_prenom
    def modifier_email(self, new_email):
        self.email=new_email
    def modifier_tel (self,new_tel):
        self.tel = new_tel
        