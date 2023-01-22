import sqlalchemy as db
from .base_model import BaseModel


class Users(BaseModel):
    """User representation."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self) -> None:
        super().__init_()
