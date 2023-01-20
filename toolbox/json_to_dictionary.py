import json

def json_to_dict(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return data