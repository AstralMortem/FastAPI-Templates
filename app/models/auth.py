from sqlalchemy.orm import Mapped, mapped_column
from .mixins import CommonUUIDMixin, BaseModel


class User(CommonUUIDMixin, BaseModel):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
