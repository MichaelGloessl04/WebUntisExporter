import webuntis
import datetime

s = webuntis.Session(server='aoide.webuntis.com',
                           username='gloess190117',
                           password='19Gloessl10!2004',
                           school='htbla-weiz',
                           useragent='mgloessl')

s.login()
today = datetime.date.today()
monday = today - datetime.timedelta(days=today.weekday())
friday = monday + datetime.timedelta(days=4)
klasse = s.klassen().filter(id=1312)[0]
foo = s.timetable(klasse=klasse, start=monday, end=friday)

for i in foo:
    print(i)