import sqlite3 as db

class Database:
    def __init__(self) -> None:
        with db.connect("timetable.db") as self.conn:
            self._cursor = self.conn.cursor()
            self._cursor.execute("""
                                 CREATE TABLE timetable.table(
                                    id INT PRIMARY KEY NOT NULL,
                                    name TEXT,
                                    start DATE,
                                    end DATE
                                 """)

    def add_lesson(self, lesson_name, lesson_start, lesson_end):
        
    