from ..tables import Timetable
from .base_model import BaseModel


class TimetableHandler(BaseModel):
    """Absence representation."""

    def __init__(self, path: str) -> None:
        super().__init__(path)
        self._table = Timetable
