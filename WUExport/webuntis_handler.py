from http import server
import webuntis

class WebUntisHandler:
    def __init__(self, server, username, password, school, useragent) -> None:
        s = webuntis.Session(server=server,
                             username=username,
                             password=password,
                             school=school,
                             useragent=useragent)
        s.login()
        self._classes = s.subjects()

    @property
    def classes(self):
        return self._classes
