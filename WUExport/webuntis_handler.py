import webuntis
import datetime
import time

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
                    if found == True:
                        break
            output.app
        return output

    def login(self):
        self._session.login()

    def logout(self):
        self._session.logout()

    def update_database(self):
        for lesson in self._timetable:
            self.db.add_lesson(self._session.subjects().filter(id=lesson.subjects[0].id)[0].name,
                               time.mktime(lesson.start.timetuple()),
                               time.mktime(lesson.end.timetuple()))
