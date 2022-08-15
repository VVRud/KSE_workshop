from datetime import timedelta
from pydantic import BaseModel


class JWTSettings(BaseModel):
    authjwt_secret_key: str = "secret"
    authjwt_denylist_enabled: bool = True
    authjwt_denylist_token_checks: set = {"access", "refresh"}
    access_expires: int = timedelta(minutes=60)
    refresh_expires: int = timedelta(days=30)


settings_obj = JWTSettings()
