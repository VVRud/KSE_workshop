from fastapi import APIRouter, Depends, HTTPException, Header
from fastapi_jwt_auth import AuthJWT

from models.user import UserAuthorize, UserData
from models.auth import AuthResponse
from db.redis import redis_conn
from db.postgres import postgres_conn
from settings.JWTSettings import settings_obj
from utils import get_tokens


router = APIRouter(prefix="/auth", tags=["authorization"])


@router.post('/signup', response_model=UserData)
def signup(
    user: UserData,
    Authorize: AuthJWT = Depends()
):
    db_user = postgres_conn.get_user(user.username)
    if db_user is not None:
        raise HTTPException(status_code=400, detail="User exist")
    postgres_conn.create_user(user)
    return user


@router.post('/login', response_model=AuthResponse)
def login(
    user: UserAuthorize,
    Authorize: AuthJWT = Depends()
):
    db_user = postgres_conn.get_user(user.username)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User do not exist")
    if db_user['password'] != user.password:
        raise HTTPException(status_code=401, detail="Bad username or password")

    access_token, refresh_token = get_tokens(user.username, Authorize)
    return {
        "access_token": access_token, "refresh_token": refresh_token,
        "detail": (
            f"Auth token will expire in {settings_obj.access_expires.total_seconds()} seconds. "
            f"Refresh token will expire in {settings_obj.refresh_expires.total_seconds()} seconds"
        )
    }


@router.post('/refresh', response_model=AuthResponse)
def refresh(
    Authorization: str = Header(...),
    Authorize: AuthJWT = Depends()
):
    Authorize.jwt_refresh_token_required()

    user = Authorize.get_jwt_subject()
    access_token, refresh_token = get_tokens(user, Authorize)
    return {
        "access_token": access_token, "refresh_token": refresh_token,
        "detail": (
            f"Auth token will expire in {settings_obj.access_expires.total_seconds()} seconds. "
            f"Refresh token will expire in {settings_obj.refresh_expires.total_seconds()} seconds"
        )
    }


@router.delete('/access-revoke', response_model=AuthResponse)
def access_revoke(
    Authorization: str = Header(...),
    Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()

    jti = Authorize.get_raw_jwt()['jti']
    redis_conn.set(jti, 'false', keepttl=True)
    return {"detail": "Access token has been revoke."}


@router.delete('/refresh-revoke', response_model=AuthResponse)
def refresh_revoke(
    Authorization: str = Header(...),
    Authorize: AuthJWT = Depends()
):
    Authorize.jwt_refresh_token_required()

    jti = Authorize.get_raw_jwt()['jti']
    redis_conn.set(jti, 'false', keepttl=True)
    return {"detail": "Refresh token has been revoke."}
