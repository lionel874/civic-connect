"""
Script à usage unique pour créer un compte admin.
Contourne volontairement la validation ROLES_PUBLICS de user_service.py,
car cette route est protégée pour empêcher la création d'admin via l'API publique.

Utilisation (depuis l'intérieur du conteneur backend) :
    docker compose exec backend python create_admin.py
"""

from CLASS.users import User
from REPOSITORIES.user_repository import create_user
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- Modifiez ces valeurs avant d'exécuter le script ---
NOM = "Admin"
PRENOM = "Civic"
EMAIL = "moudouthefelix3@gmail.com"
TEL = "612345678"
MOT_DE_PASSE = "ayana erna3"  # à changer après le premier test si besoin
# ---------------------------------------------------------

mot_de_passe_hash = pwd_context.hash(MOT_DE_PASSE)

utilisateur = User(
    nom=NOM,
    prenom=PRENOM,
    email=EMAIL,
    tel=TEL,
    role="admin",
    mot_de_passe=mot_de_passe_hash,
)

resultat = create_user(utilisateur)
print(f"Compte admin créé avec succès : {EMAIL}")