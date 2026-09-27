from fastapi import APIRouter, Depends

from auth import get_current_admin


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/dashboard", summary="Tableau de bord administrateur")
def dashboard(admin_id: int = Depends(get_current_admin)):
    return {
        "message": "Bienvenue dans le tableau de bord administrateur",
        "admin_id": admin_id
    }