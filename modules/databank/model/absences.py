import sqlalchemy as db
from .base_model import BaseModel


class Absences(BaseModel):
    """Absence representation."""

    __tablename__ = "absences"
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Time)
    end = db.Column(db.Time)

    def init(self):
        self._table_name = "absences"
