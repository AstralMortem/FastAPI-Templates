from .mixins import CommonUUIDMixin, BaseModel


class User(CommonUUIDMixin, BaseModel):
    __tablename__ = "users"
