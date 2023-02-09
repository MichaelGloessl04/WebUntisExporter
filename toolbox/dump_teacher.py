from toolbox import json_to_dict


def _dump_teacher_names(self):
    stack = json_to_dict(
        "C:/Code/WebUntisExporter/toolbox/teacher_id_name.json")
    for key in stack.keys():
        self.append(id=int(key),
                    short_name=stack[key][0],
                    long_name=stack[key][1])
