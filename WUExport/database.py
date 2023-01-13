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
        # Connect to the database
        conn = db.connect('timetable.db')

        # Create a cursor object
        cursor = conn.cursor()

        # Execute the "SELECT name FROM sqlite_master WHERE type='table'" query
        cursor.execute("""SELECT
                            name,
                            start,
                            end
                        FROM
                            timetable
                        ORDER BY
                            start DESC;""")

        # Fetch all the results
        table = cursor.fetchall()
        table.reverse()

        # Print the names of all the tables
        for lessons in table:
            now = "{0} | {1} | {2}".format(lessons[0], datetime.fromtimestamp(int(lessons[1])), datetime.fromtimestamp(int(lessons[2])))
            if lessons is table[0]:
                print(now)
                last = now
            elif last is not now:
                print(now)
                last = now
            

        # Close the cursor and the connection
        cursor.close()
        conn.close()