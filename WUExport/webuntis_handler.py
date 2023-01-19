import webuntis
import datetime
import time

class WebUntisHandler:
    def __init__(self, server, username, password, school) -> None:
        self.school = webuntis.Session(server=server,
                             username=username,
                             password=password,
                             school=school,
                             useragent=username)
        self.school.login()
        today = datetime.date.today()
        monday = today - datetime.timedelta(days=today.weekday())
        friday = monday + datetime.timedelta(days=4)
        klasse = self.school.klassen().filter(id=1312)[0]
        self._timetable = self.school.timetable(klasse=klasse, start=monday, end=friday)

    @property
    def timetable(self):
        return self._timetable.to_table()

    def update_database(self):
        self.db.clear_table()
        for lesson in self._timetable:
            self.db.add_lesson(self.school.subjects().filter(id=lesson.subjects[0].id)[0].name,
                               time.mktime(lesson.start.timetuple()),
                               time.mktime(lesson.end.timetuple()))
        self.db.print_table()

    def clear_database(self):
        self.db.clear_table()

    def print_database(self):
        self.db.print_table()
