from ..tables import Subjects
from .base_model import BaseModel


class SubjectHandler(BaseModel):
    """Absence representation."""

    def __init__(self, path: str) -> None:
        super().__init__(path)
        self._table = Subjects
