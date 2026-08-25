from database import SessionLocal
from CLASS.users import User




# creation d'un user dans la base de donnee

def create_user(utilsateur):
    db =SessionLocal()
    try:
     db.add(utilsateur)
     db.commit()
     db.refresh(utilsateur)
     return utilsateur
    finally:
        db.close()

def identifier_user_par_id(user_id:int ): 
      db =SessionLocal()
      try:
        utilisateur = db.get(User,user_id)

        return utilisateur
      finally:
          db.close

def modif_user_repository(user_id,
                          nom,
                          prenom,
                          email,

                          tel,
                          role):
      
       db = SessionLocal() 
       try:

        utilisateur = db.query(User).filter(
            User.id == user_id
        ).first()

        if utilisateur is None:
            return None

        utilisateur.nom = nom
        utilisateur.prenom = prenom
        utilisateur.email = email
        utilisateur.tel = tel
        utilisateur.role = role

        db.commit()
        db.refresh(utilisateur)

        return utilisateur
       finally:
           db.close()


#lire tout les user dans la bd 


def lire_users_repository():
      db = SessionLocal()
      try:
       return db.query(User).all()
      finally:
          db.close()

# supprimer un user a paertie de son id

 
def supprimer_user_repository(user_id):
    db = SessionLocal()
        
    
    try:

        user = db.query(User).filter(
            User.id == user_id
        ).first()

        if user is None:
            return None

        db.delete(user)
        db.commit()

        return {
            "message": "Utilisateur supprimé avec succès"
        }

    finally:
        db.close()


def patch_user_repository(
    user_id,
    nouveau_nom=None,
    nouveau_prenom=None,
    nouveau_email=None,
    nouveau_tel=None,
    nouveau_role=None
):
    db = SessionLocal()

    try:
        utilisateur = db.query(User).filter(
            User.id == user_id
        ).first()

        if utilisateur is None:
            return None

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

        db.commit()
        db.refresh(utilisateur)

        return utilisateur

    finally:
        db.close()