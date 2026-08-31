from fastapi import APIRouter

from SERVICES.user_service import (ajout_user, 
                                   modifier_user_service,
                                   supprimer_user_service,
                                   lire_users_service,
                                   patch_user_service)

router = APIRouter(
    prefix= "/users",
    tags=["Users"]
)

@router.post("/",summary="Créer un utilisateur")


def create_user(nom: str,
                prenom: str,
                email: str,
                tel:str,
                role: str ):
    """Crée un nouvel utilisateur dans l'application."""  
    return ajout_user(nom, 
                      prenom, 
                      email, 
                      tel, 
                      role)


@router.patch("/{user_id}",summary="Modifier partiellement un utilisateur")
def patch_user(
    user_id: int,
    nouveau_nom: str | None = None,
    nouveau_prenom: str | None = None,
    nouveau_email: str | None = None,
    nouveau_tel: str | None = None,
    nouveau_role: str | None = None,
    
):
    """Modifie un ou plusieurs champs d'un utilisateur, sans toucher aux autres."""  
    return patch_user_service(
        user_id,
        nouveau_nom,
        nouveau_prenom,
        nouveau_email,
        nouveau_tel,
        nouveau_role,
        
    )

@router.get("/",summary="Lister les utilisateurs")
def get_users():
  """Retourne la liste de tous les utilisateurs."""
  return lire_users_service()



@router.delete("/{user_id}",summary="Supprimer un utilisateur")
def delete_user(user_id:int ):
    """Supprime un utilisateur par son identifiant."""
    return supprimer_user_service(user_id)

@router.put("/{user_id}",summary="Remplacer un utilisateur")
def update_user(
    user_id: int,
    nouveau_nom: str,
    nouveau_prenom: str,
    nouveau_email: str,
    nouveau_tel: str,
    nouveau_role: str
):
    """Remplace entièrement les informations d'un utilisateur existant."""

    return modifier_user_service(
        user_id,
        nouveau_nom,
        nouveau_prenom,
        nouveau_email,
        nouveau_tel,
        nouveau_role
    )
    