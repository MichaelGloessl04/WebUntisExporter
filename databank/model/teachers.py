from ..tables import Teachers
from .base_model import BaseModel


class TeacherHandler(BaseModel):
    """Absence representation."""

    def __init__(self, path: str) -> None:
        super().__init__(path)
        self._table = Teachers
