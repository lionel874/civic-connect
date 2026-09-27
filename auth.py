from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os

SECRET_KEY = os.getenv("SECRET_KEY", "une_valeur_par_defaut_dev_uniquement")

ALGORITHM = "HS256"
DUREE_TOKEN_MINUTES = 30

security_scheme = HTTPBearer()


def creer_token(user_id: int, role: str) -> str:
    expiration = datetime.utcnow() + timedelta(minutes=DUREE_TOKEN_MINUTES)
    payload = {"sub": str(user_id), "role": role, "exp": expiration}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security_scheme)) -> int:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token invalide")
        return int(user_id)
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalide ou expiré")


def get_current_admin(
    credentials: HTTPAuthorizationCredentials = Depends(security_scheme)
) -> int:

    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user_id = payload.get("sub")
        role = payload.get("role")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Token invalide"
            )

        if role != "admin":
            raise HTTPException(
                status_code=403,
                detail="Accès réservé aux administrateurs"
            )

        return int(user_id)

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token invalide ou expiré"
        )

def get_current_user_with_role(
    credentials: HTTPAuthorizationCredentials = Depends(security_scheme)
) -> dict:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        role = payload.get("role")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token invalide")
        return {"id": int(user_id), "role": role}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalide ou expiré")