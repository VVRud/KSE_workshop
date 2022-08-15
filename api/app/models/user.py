from pydantic import BaseModel


class UserAuthorize(BaseModel):
    username: str
    password: str


class UserData(UserAuthorize):
    name: str
    city: str
    occupation: str
