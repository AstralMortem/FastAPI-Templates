from uuid import UUID
from pydantic import BaseModel, ConfigDict


class SUserInsert(BaseModel):
    email: str
    password: str


class SUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    email: str


class Credentials(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
