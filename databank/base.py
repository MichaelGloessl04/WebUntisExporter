import sqlalchemy as db
from .model import Base as base
import inspect

class Base:
    def __init__(self) -> None:
        self._implemented_check()
        self._table_name = None
        self._model = None
        self._colums = []
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
        return query.keys()

    def _implemented_check(self):
        if type(self) == Base:
            raise NotImplementedError

    def append(self):
        self._implemented_check()
        sig = inspect.signature(self.append)
        items = sig.parameters.items()
        with self.session_factory() as session:
            session.insert(self.Model).\
                    values()
            session.commit()

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
