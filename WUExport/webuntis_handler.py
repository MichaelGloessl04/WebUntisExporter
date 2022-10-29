import webuntis
import datetime

class WebUntisHandler:
    def __init__(self, server, username, password, school, useragent) -> None:
        s = webuntis.Session(server=server,
                             username=username,
                             password=password,
                             school=school,
                             useragent=useragent)
        s.login()
        today = datetime.date.today()
        monday = today - datetime.timedelta(days=today.weekday())
        friday = monday + datetime.timedelta(days=4)
        klasse = s.klassen().filter(id=1312)[0]
        self._timetable = s.timetable(klasse=klasse, start=monday, end=friday)

    @property
    def timetable(self):
        return self._timetable.to_table()
