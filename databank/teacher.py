from .model import Teachers
from .base import Base


class Teacher(Base):
    def __init__(self) -> None:
        super().__init__()
        self._table_name = "teachers"

    def append(self, id, short_name, long_name):
        with self.session_factory() as session:
            new_teacher = Teachers(id=id,
                                   short_name=short_name,
                                   long_name=long_name)
            session.add(new_teacher)
            session.commit()
