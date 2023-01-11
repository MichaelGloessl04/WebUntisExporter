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
subjects = s.subjects()

for lesson in foo:
    try:
        print(s.subjects().filter(id=lesson.subjects[0].id))
    except Exception as e:
        print(e)
