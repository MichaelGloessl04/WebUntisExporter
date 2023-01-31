import sqlalchemy as db
from .base_model import BaseModel
from .models import Absences as table


class Absences(BaseModel):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self._table = table
