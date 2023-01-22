import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
import inspect


Base = declarative_base()


class BaseModel(Base):
    def __init__(self) -> None:
        self._implemented_check()
        self._model = None
        db_connection = db.create_engine("sqlite:///databank/databank.db")
        base.metadata.create_all(db_connection)
        self.session_factory = db.orm.sessionmaker()
        self.session_factory.configure(bind=db_connection)

    @property
    def Table_Name(self):
        self._implemented_check()
        return self._table_name

    @property
    def Model(self):
        self._implemented_check()
        return self._model

    @property
    def Column_Names(self):
        self._implemented_check()
        query = db.select([self.Model]).select_more(self.Model)
        return query

    def _implemented_check(self):
        if type(self) == Base:
            raise NotImplementedError

    def append(self):
        self._implemented_check()
        keys = list(inspect.signature(self.append).parameters.get())
        with self.session_factory() as session:
            session.add(self.Model())

    def delete(self, column: str, value: any):
        """Deletes rows based on the given column and value."""
        self._implemented_check()
        with self.session_factory() as session:
            session.query(self.Model).filter(
                getattr(self.Model, column) == value
                ).delete(synchronize_session="fetch")
            session.commit()

    def delete_all(self):
        self._implemented_check()
        with self.session_factory() as session:
            session.query(self.Model).delete(synchronize_session="fetch")
            session.commit()
