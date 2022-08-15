from fastapi import FastAPI, Request, Depends, Header
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException

from db.redis import redis_conn
from db.postgres import postgres_conn
from settings.JWTSettings import settings_obj
from models.status import Status
from routers import auth, data


app = FastAPI(debug=True)


@app.get("/status", response_model=Status)
def status(
    Authorization: str = Header(...),
    Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()
    return {
        "api_status": "ok",
        "redis_status": "ok" if redis_conn.check_status() else "not_ok",
        "postgres_status": "ok" if postgres_conn.check_status() else "not_ok"
    }


@AuthJWT.load_config
def get_config():
    return settings_obj


@AuthJWT.token_in_denylist_loader
def check_if_token_in_denylist(decrypted_token):
    jti = decrypted_token['jti']
    entry = redis_conn.get(jti)
    return entry is None or entry == 'false'


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


app.include_router(auth.router)
app.include_router(data.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)
