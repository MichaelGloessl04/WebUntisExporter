import sqlite3 as db

class Database:
    def __init__(self) -> None:
        with db.connect("timetable.db") as _conn:
            _cursor = _conn.cursor()
            _cursor.execute("""
                                CREATE TABLE IF NOT EXISTS timetable (
                                    id INT PRIMARY KEY NOT NULL,
                                    name TEXT,
                                    start INT,
                                    end INT
                                );
                                """)

    def add_lesson(self, lesson_name, lesson_start, lesson_end):
        print(lesson_start)
        print(lesson_end)
        with db.connect("timetable.db") as _conn:
            _cursor = _conn.cursor()
            scpt = "INSERT INTO timetable VALUES ({0}, {1}, {2})".format(lesson_name, lesson_start, lesson_end)
            _cursor.execute(scpt)

    def clear_table(self, table_name):
        with db.connect("timetable.db") as _conn:
            _cursor = _conn.cursor()
            _cursor.execute("DELETE FROM \"%s\"" % table_name)