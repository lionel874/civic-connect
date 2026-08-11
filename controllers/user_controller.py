from sqlalchemy.orm import Session
from CLASS.users import User
from database import engine



def modifier_user(user_id, nouveau_nom, nouveau_prenom, nouveau_email,nouveau_tel,nouveau_role ):
    with Session(engine) as session:
        user = session.get(User,user_id)
        if user is None:
            print("utilisateur introuvable")
            return
        user.nom = nouveau_nom
        user.prenom = nouveau_prenom
        user.email = nouveau_email
        user.tel = nouveau_tel
        user.role = nouveau_role

        session.commit()


def ajout_user(nom, prenom, email, tel, role, db_engine=engine):
    with Session(db_engine) as session:
        if not nom:
            raise ValueError("le nom est obligatoire")
        
        if not prenom:
          raise ValueError("Le prénom est obligatoire")

        if not email:
          raise ValueError("L'email est obligatoire")
 
        if not tel:
          raise ValueError("Le téléphone est obligatoire")

        if not role:
           raise ValueError("Le rôle est obligatoire")
        
        
        # pour verifier si ls nom est une chaine de caractere


        if not isinstance(nom, str):
          raise ValueError("Le nom doit être une chaîne de caractères")

        
        utilisateur = User( 
                           nom=nom,
                           prenom=prenom,
                           email=email,
                           tel=tel,
                           role=role)
        session.add(utilisateur)
        session.commit()
        return utilisateur





