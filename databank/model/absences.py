from ..tables import Absences
from .base_model import BaseModel


class AbsenceHandler(BaseModel):
    """Absence representation."""

    def __init__(self, path: str) -> None:
        super().__init__(path)
        self._table = Absences
