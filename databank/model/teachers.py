import sqlalchemy as db
from .base_model import BaseModel
from toolbox import json_to_dict


class Teachers(BaseModel):
    """Teacher representation."""

    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True)
    long_name = db.Column(db.String)
    short_name = db.Column(db.String)

    def _dump_teacher_names(self):
        stack = json_to_dict(
            "C:/Code/WebUntisExporter/toolbox/teacher_id_name.json")
        for key in stack.keys():
            self.append(id=int(key),
                        short_name=stack[key][0],
                        long_name=stack[key][1])
