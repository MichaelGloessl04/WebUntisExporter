import sqlalchemy as db
from .base_model import BaseModel


class Todos(BaseModel):
    """TODOs representation."""

    __tablename__ = "TODOs"
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.Integer,
                        db.ForeignKey("subjects.id"),
                        nullable=False)
    description = db.Column(db.String)
    start = db.Column(db.Time)
    end = db.Column(db.Time)
    colour = db.Column(db.String)

    def __init__(self) -> None:
        super().__init_()
