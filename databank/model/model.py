import sqlalchemy as db
import sqlalchemy.ext.declarative

Base = sqlalchemy.ext.declarative.declarative_base()


class Timetable(Base):
    """Timetable representation."""

    __tablename__ = "timetable"
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.Integer,
                        db.ForeignKey("subjects.id"),
                        nullable=False)
    start = db.Column(db.Time)
    end = db.Column(db.Time)
    teacher = db.Column(db.Integer,
                        db.ForeignKey("teachers.id"),
                        nullable=False)


class Todos(Base):
    """TODOs representation."""

    __tablename__ = "TODOs"
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.Integer,
                        db.ForeignKey("subjects.id"),
                        nullable=False)
    description = db.Column(db.String)
    start = db.Column(db.Time)
    end = db.Column(db.Time)
    colour = db.Column(db.String)


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


class Absences(Base):
    """Absence representation."""

    __tablename__ = "absences"
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Time)
    end = db.Column(db.Time)


class Users(Base):
    """User representation."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)