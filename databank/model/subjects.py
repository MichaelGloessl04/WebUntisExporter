import sqlalchemy as db
from .base_model import BaseModel


class Subjects(BaseModel):
    """Subject representation."""

    __tablename__ = "subjects"
    id = db.Column(db.Integer, primary_key=True)
    long_name = db.Column(db.String)
    short_name = db.Column(db.String)

    def __init__(self) -> None:
        super().__init__()
