import os


def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
