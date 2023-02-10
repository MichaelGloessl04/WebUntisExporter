import webuntis
import datetime
import time
from databank.model import *  # noqa: F403


class WebUntisHandler:
    def __init__(self, server, username, password, school) -> None:
        self._session = webuntis.Session(server=server,
                                         username=username,
                                         password=password,
                                         school=school,
                                         useragent=username)

    @property
    def timetable(self):
        today = datetime.date.today()
        monday = today - datetime.timedelta(days=today.weekday())
        friday = monday + datetime.timedelta(days=4)
        klasse = self._session.klassen().filter(id=1312)[0]
        return self._session.timetable(klasse=klasse, start=monday, end=friday)

    @property
    def teacher_id(self):
        ph = self.timetable
        output = []
        for lesson in ph:
            found = False
            parts = str(lesson).split('\'te\'')
            out = ""
            for letter in parts[1]:
                try:
                    int(letter)
                    out += letter
                    found = True
                except ValueError:
                    if found is True:
                        break
            output.app
        return output

    def login(self):
        self._session.login()

    def logout(self):
        self._session.logout()

    def update_database(self):
        t = TimetableHandler("C:/Code/WebUntisExporter/databank/databank.db")  # noqa: F405
        for lesson in self.timetable:
            subject_id = lesson.subjects[0].id
            start = int(time.mktime(lesson.start.timetuple()))
            end = int(time.mktime(lesson.end.timetuple()))
            teacher_id = 0
            t.append(subject=subject_id, start=start, end=end, teacher=teacher_id)

    def _dump_subjects(self):
        s = self._session.subjects()
        subjects = SubjectHandler("C:/Code/WebUntisExporter/databank/databank.db")  # noqa: F405
        for subject in s:
            subjects.append(id=subject.id, short_name=subject.name, long_name=subject.long_name)
