from fastapi import APIRouter
from fastapi import APIRouter, Depends
from auth import get_current_admin
from auth import get_current_admin, get_current_user_with_role
from fastapi import APIRouter, Depends, HTTPException
from SERVICES.user_service import (ajout_user, 
                                   modifier_user_service,
                                   supprimer_user_service,
                                   lire_users_service,
                                   patch_user_service,login_service)

router = APIRouter(
    prefix= "/users",
    tags=["Users"]
)

@router.post("/",summary="Créer un utilisateur")


def create_user(nom: str,
                prenom: str,
                email: str,
                tel:str,
                role: str,
                mot_de_passe: str  ):
    """Crée un nouvel utilisateur dans l'application."""  
    return ajout_user(nom, 
                      prenom, 
                      email, 
                      tel, 
                      role,
                      mot_de_passe)

@router.post("/login", summary="Se connecter")
def login(email: str, mot_de_passe: str):
    """Vérifie les identifiants et retourne un token valide 30 minutes."""
    return login_service(email, mot_de_passe)

@router.patch("/{user_id}", summary="Modifier partiellement un utilisateur")
def patch_user(
    user_id: int,
    nouveau_nom: str | None = None,
    nouveau_prenom: str | None = None,
    nouveau_email: str | None = None,
    nouveau_tel: str | None = None,
    nouveau_role: str | None = None,
    current_user: dict = Depends(get_current_user_with_role)
):
    """Modifie un ou plusieurs champs d'un utilisateur, sans toucher aux autres."""
    if current_user["role"] != "admin" and current_user["id"] != user_id:
        raise HTTPException(status_code=403, detail="Vous ne pouvez modifier que votre propre profil")

    return patch_user_service(
        user_id,
        nouveau_nom,
        nouveau_prenom,
        nouveau_email,
        nouveau_tel,
        nouveau_role,
    )

@router.get("/", summary="Lister les utilisateurs")
def get_users(admin_id: int = Depends(get_current_admin)):
    """Retourne la liste de tous les utilisateurs."""
    return lire_users_service()


@router.delete("/{user_id}",summary="Supprimer un utilisateur")
def delete_user(
    user_id: int,
    admin_id: int = Depends(get_current_admin)
):
    """Supprime un utilisateur par son identifiant."""
    return supprimer_user_service(user_id)

@router.put("/{user_id}", summary="Remplacer un utilisateur")
def update_user(
    user_id: int,
    nouveau_nom: str,
    nouveau_prenom: str,
    nouveau_email: str,
    nouveau_tel: str,
    nouveau_role: str,
    current_user: dict = Depends(get_current_user_with_role)
):
    """Remplace entièrement les informations d'un utilisateur existant."""
    if current_user["role"] != "admin" and current_user["id"] != user_id:
        raise HTTPException(status_code=403, detail="Vous ne pouvez modifier que votre propre profil")

    return modifier_user_service(
        user_id,
        nouveau_nom,
        nouveau_prenom,
        nouveau_email,
        nouveau_tel,
        nouveau_role
    )