import sqlalchemy as db
import sqlalchemy.ext.declarative
from sqlalchemy.orm import relationship

Base = sqlalchemy.ext.declarative.declarative_base()


class Timetable(Base):
    """Timetable representation."""

    __tablename__ = "timetable"
    id = db.Column(db.Integer, primary_key=True)
    subject = relationship("Subjects", backref="Subjects")
    start = db.Column(db.Integer)
    end = db.Column(db.Integer)
    teacher = relationship("Teachers", backref="")


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
