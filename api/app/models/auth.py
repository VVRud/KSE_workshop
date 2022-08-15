from typing import Optional
from pydantic import BaseModel


class AuthResponse(BaseModel):
    access_token: Optional[str]
    refresh_token: Optional[str]
    detail: str
