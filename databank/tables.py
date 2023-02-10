import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Absences(Base):
    """Absence representation."""

    __tablename__ = "absences"
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Integer)
    end = db.Column(db.Integer)


class Subjects(Base):
    """Subject representation."""

    __tablename__ = "subjects"
    id = db.Column(db.Integer, primary_key=True)
    long_name = db.Column(db.String)
    short_name = db.Column(db.String)


class Teachers(Base):
    """Teacher representation."""

    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True)
    long_name = db.Column(db.String)
    short_name = db.Column(db.String)


class Timetable(Base):
    """Timetable representation."""

    __tablename__ = "timetable"
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.Integer,
                        db.ForeignKey("subjects.id"),
                        nullable=False)
    start = db.Column(db.Integer)
    end = db.Column(db.Integer)
    teacher = db.Column(db.Integer,
                        db.ForeignKey("teachers.id"),
                        nullable=False)
