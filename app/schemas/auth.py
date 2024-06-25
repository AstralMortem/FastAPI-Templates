from uuid import UUID
from pydantic import BaseModel


class SUser(BaseModel):
    id: UUID
