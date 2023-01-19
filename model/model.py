import sqlalchemy
import sqlalchemy.ext.declarative
from sqlalchemy.orm import relationship

Base = sqlalchemy.ext.declarative.declarative_base()


class Timetable(Base):
    """Student representation."""

    __tablename__ = "student"
    student_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String)
    sure_name = sqlalchemy.Column(sqlalchemy.String)
    emails = relationship("Email", backref="Email")

    def __repr__(self):
        """Get representation."""
        return "<Student: %s %s>" % (self.first_name, self.sure_name)


class Email(Base):
    """Email address representation."""

    __tablename__ = "email"
    email_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    email = sqlalchemy.Column(sqlalchemy.String)
    student_id = sqlalchemy.Column(sqlalchemy.Integer,
                                   sqlalchemy.ForeignKey("student.student_id"),
                                   nullable=False)