from sqlalchemy.orm import Session
from CLASS.users import User




# creation d'un user dans la base de donnee

def create_user(utilsateur:User, session:Session):
    
     session.add(utilsateur)
     session.commit()
     session.refresh(utilsateur)
     return utilsateur

def identifier_user_par_id(user_id:int, session:Session ):
   
      utilisateur = session.get(User,user_id)

      return utilisateur

def modif_user_repository(utilisateur: User, session:Session):
      
         user = session.get(User, utilisateur.id) 
         if user is None:
            return None
         
      
         user.nom = utilisateur.nom
         user.prenom = utilisateur.prenom
         user.email = utilisateur.email
         user.tel = utilisateur.tel
         user.role = utilisateur.role

         session.commit()
         session.refresh(user)

         return user