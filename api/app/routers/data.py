from fastapi import APIRouter, Depends, Header
from fastapi_jwt_auth import AuthJWT

from db.postgres import postgres_conn


router = APIRouter(prefix="/data", tags=["data"])


@router.get('/user')
def protected(
        Authorization: str = Header(...),
        Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    user = postgres_conn.get_user(current_user)
    del user["id"]

    return user
