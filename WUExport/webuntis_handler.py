import webuntis
import datetime
from database import Database

class WebUntisHandler:
    def __init__(self, server, username, password, school, useragent) -> None:
        self.db = Database()
        self.school = webuntis.Session(server=server,
                             username=username,
                             password=password,
                             school=school,
                             useragent=useragent)
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
        for lesson in self._timetable:
            self.db.add_lesson(self.school.subjects().filter(id=lesson.subjects[0].id)[0].name,
                               lesson.start,
                               lesson.end)
