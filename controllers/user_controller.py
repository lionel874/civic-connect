
from CLASS.users import User
from  SERVICES.user_service import ajout_user
from SERVICES.user_service import modifier_user_service


        


def ajout_user(nom, prenom, email, tel, role, ):

   return ajout_user(nom, prenom, email, tel, role)


def modif_user(user_id, 
               nouveau_nom,
               nouveau_prenom,
               nouveau_email,
               nouveau_tel,
               nouveau_role
               
               ):
     return modifier_user_service(user_id,
                          nouveau_nom,
                          nouveau_prenom,
                          nouveau_email,
                          nouveau_tel,
                          nouveau_role)