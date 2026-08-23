
from CLASS.users import User
from REPOSITORIES.user_repository import create_user
from REPOSITORIES.user_repository import modif_user_repository,identifier_user_par_id,lire_users_repository
from REPOSITORIES.user_repository import supprimer_user_repository
from sqlalchemy.orm import Session
def ajout_user(nom, prenom, email, tel, role, session:Session):
    
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
        

        if isinstance (tel, int):
           raise ValueError("numero de tel en chifffre")
        
      
        
        if not isinstance(tel, str):
         raise ValueError("Le téléphone doit être une chaîne de caractères")

        if not tel.isdigit():
         raise ValueError(
        "Le téléphone doit contenir uniquement des chiffres"
    )
# pour verifier si le numero commence par 6

        if not tel.startswith("6"):
         raise ValueError(
        "Le téléphone doit commencer par 6"
    )
        

        roles_autorises = ["user", "admin", "provider"]

        if role not in roles_autorises:
         raise ValueError("Rôle invalide")

        if "@" not in email or "." not in email:
         raise ValueError("L'adresse email est invalide")
        
        utilisateur = User( 
                           nom=nom,
                           prenom=prenom,
                           email=email,
                           tel=tel,
                           role=role,
                           )
        
        return create_user(utilisateur,session)


def modifier_user_service(
    user_id,
    nouveau_nom,
    nouveau_prenom,
    nouveau_email,
    nouveau_tel,
    nouveau_role,
    session: Session
):

    if not nouveau_nom:
        raise ValueError("Le nom est obligatoire")

    if not nouveau_prenom:
        raise ValueError("Le prénom est obligatoire")

    if not nouveau_email:
        raise ValueError("L'email est obligatoire")

    if not nouveau_tel:
        raise ValueError("Le numéro est obligatoire")

    if not nouveau_role:
        raise ValueError("Le rôle est obligatoire")

    utilisateur = identifier_user_par_id(
        user_id,
        session
    )

    if utilisateur is None:
        raise ValueError("Utilisateur introuvable")

    utilisateur.nom = nouveau_nom
    utilisateur.prenom = nouveau_prenom
    utilisateur.email = nouveau_email
    utilisateur.tel = nouveau_tel
    utilisateur.role = nouveau_role

    return modif_user_repository(
        utilisateur,
        session
    )


# fonction qui L'ensemble des utilisateur

def lire_users_service(session:Session):
   return lire_users_repository (session)

# fonction supprimer un utilisateur a parti de son id


def supprimer_user_service(user_id: int, session: Session):

    utilisateur = identifier_user_par_id(user_id, session)

    if utilisateur is None:
        raise ValueError("Utilisateur introuvable")

    return supprimer_user_repository(user_id, session)

def patch_user_service(
    user_id,
    nouveau_nom=None,
    nouveau_prenom=None,
    nouveau_email=None,
    nouveau_tel=None,
    nouveau_role=None,
    session: Session = None
):

    utilisateur = identifier_user_par_id(
        user_id,
        session
    )

    if utilisateur is None:
        raise ValueError("Utilisateur introuvable")

    if nouveau_nom is not None:
        utilisateur.nom = nouveau_nom

    if nouveau_prenom is not None:
        utilisateur.prenom = nouveau_prenom

    if nouveau_email is not None:
        utilisateur.email = nouveau_email

    if nouveau_tel is not None:
        utilisateur.tel = nouveau_tel

    if nouveau_role is not None:
        utilisateur.role = nouveau_role

    return modif_user_repository(
        utilisateur,
        session
    )
