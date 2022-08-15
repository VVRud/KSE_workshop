from fastapi_jwt_auth import AuthJWT
from db.redis import redis_conn
from settings.JWTSettings import settings_obj
from models.user import UserAuthorize


def get_tokens(user: UserAuthorize, Authorize: AuthJWT):
    access_token = Authorize.create_access_token(subject=user)
    refresh_token = Authorize.create_refresh_token(subject=user)

    redis_conn.setex(
        Authorize.get_raw_jwt(access_token)['jti'],
        settings_obj.access_expires, 'true'
    )

    redis_conn.setex(
        Authorize.get_raw_jwt(refresh_token)['jti'],
        settings_obj.refresh_expires, 'true'
    )

    return access_token, refresh_token
