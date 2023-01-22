from .model import Teachers
from .base import Base
from toolbox import json_to_dict


class Teacher(Base):
    def __init__(self) -> None:
        super().__init__()
        self._model = Teachers

    def append(self, id, long_name, short_name):
        return super().append()

    def _dump_teacher_names(self):
        stack = json_to_dict(
            "C:/Code/WebUntisExporter/toolbox/teacher_id_name.json")
        for key in stack.keys():
            self.append(int(key), stack[key][0], stack[key][1])
