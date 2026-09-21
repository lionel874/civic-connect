from fastapi import APIRouter, Query, Depends
from auth import get_current_user

from SERVICES.point_connectivite_service import (
    ajout_point_connectivite_service,
    lire_point_connectivite_service,
    supprimer_point_connectivite_service
)


router = APIRouter(
    prefix="/connectivite",
    tags=["Connectivite"]
)


@router.post("/", summary="Ajouter un point de connectivité")
def create_point_connectivite(
    nom: str,
    qualite_reseau: str,
    horaires: str,
    ville: str,
    quartier: str,
    user_id: int = Depends(get_current_user),
):
    """Ajoute un point de connectivité (cybercafé, zone wifi...) pour l'utilisateur connecté."""
    return ajout_point_connectivite_service(
        nom=nom,
        qualite_reseau=qualite_reseau,
        horaires=horaires,
        user_id=user_id,
        ville=ville,
        quartier=quartier,
    )


@router.get("/", summary="Lister les points de connectivité")
def get_points_connectivite(
    ville: str = Query(None, description="Filtrer par ville", example="Dschang"),
    qualite_reseau: str = Query(None, description="Filtrer par qualité réseau", example="Bon"),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
):
    """Retourne la liste des points de connectivité, avec filtres optionnels."""
    return lire_point_connectivite_service(ville, qualite_reseau, page, limit)


@router.delete("/{point_id}", summary="Supprimer un point de connectivité")
def delete_point_connectivite(point_id: int):
    """Supprime un point de connectivité par son identifiant."""
    return supprimer_point_connectivite_service(point_id)