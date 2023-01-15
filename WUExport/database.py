import sqlite3 as db
from datetime import datetime

class Database:
    def __init__(self) -> None:
        with db.connect("timetable.db") as _conn:
            _cursor = _conn.cursor()
            _cursor.execute("""
                                CREATE TABLE IF NOT EXISTS timetable (
                                    id INTEGER PRIMARY KEY NOT NULL,
                                    name TEXT,
                                    start INT,
                                    end INT
                                );
                                """)

    def add_lesson(self, lesson_name, lesson_start, lesson_end):
        with db.connect("timetable.db") as _conn:
            _cursor = _conn.cursor()
            scpt = """INSERT INTO timetable (name, start, end)
                      VALUES
                          ('{0}', {1}, {2});
                   """.format(lesson_name, lesson_start, lesson_end)
            _cursor.execute(scpt)
            _conn.commit()

    def clear_table(self):
        with db.connect("timetable.db") as _conn:
            _cursor = _conn.cursor()
            _cursor.execute("DELETE FROM timetable")
            _conn.commit()

    def print_table(self):
        last = None
        with db.connect('timetable.db') as conn:
            cursor = conn.cursor()

            cursor.execute("""
                           SELECT
                              name,
                              start,
                              end
                           FROM
                              timetable
                           ORDER BY
                              start DESC;
                           """)

            table = cursor.fetchall()
            table.reverse()

            for lesson in table:
                now = lesson
                start = self._unix_to_datetime(now[1])
                end = self._unix_to_datetime(now[2])
                stmt = "{0} | {1} | {2}".format(lesson[0], start, end)
                
                if lesson is table[0]:
                    print(stmt)
                    last = now
                elif last != now:
                    if self._unix_to_datetime(last[1]).day != start.day:
                        print('-------------%s.%s.%s------------' % (start.day, start.month, start.year))
                    print(stmt)
                    last = now

    def _unix_to_datetime(self, unix):
        return datetime.fromtimestamp(int(unix))
