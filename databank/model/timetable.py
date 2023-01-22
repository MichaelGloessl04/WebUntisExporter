import sqlalchemy as db
from .base_model import BaseModel


class Timetable(BaseModel):
    """Timetable representation."""

    __tablename__ = "timetable"
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.Integer,
                        db.ForeignKey("subjects.id"),
                        nullable=False)
    start = db.Column(db.Time)
    end = db.Column(db.Time)
    teacher = db.Column(db.Integer,
                        db.ForeignKey("teachers.id"),
                        nullable=False)

    def __init__(self) -> None:
        super().__init_()
