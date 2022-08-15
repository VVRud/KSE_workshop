from pydantic import BaseModel


class Status(BaseModel):
    api_status: str
    redis_status: str
    postgres_status: str
