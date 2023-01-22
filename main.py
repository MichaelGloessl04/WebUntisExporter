import databank.model as models
from datetime import datetime as dt


def main():
    t = models.Teachers()
    t._dump_teacher_names()
    timetable = models.Timetable()
    timetable.append(subject=12, start=dt.now(), end=dt.now(), teacher=131)


if __name__ == "__main__":
    main()
