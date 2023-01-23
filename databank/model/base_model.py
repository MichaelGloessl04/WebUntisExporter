import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    global session_factory

    db_connection = db.create_engine("sqlite:///databank/databank.db")
    Base.metadata.create_all(bind=db_connection)
    session_factory = db.orm.sessionmaker()
    session_factory.configure(bind=db_connection)

    @property
    def Table_Name(self):
        self._implemented_check()
        return self._table_name

    @property
    def Model(self):
        self._implemented_check()
        return type(self)

    @property
    def Column_Names(self):
        self._implemented_check()
        query = db.select([self.Model]).select_more(self.Model)
        return query

    def _implemented_check(self):
        if type(self) == Base:
            raise NotImplementedError

    def append(self, **collumns):
        with session_factory() as session:
            row = self.Model(**collumns)
            session.add(row)
            session.commit()

    def delete(self, column: str, value: any):
        """Deletes rows based on the given column and value."""
        self._implemented_check()
        with session_factory() as session:
            session.query(self.Model).filter(
                getattr(self.Model, column) == value
                ).delete(synchronize_session="fetch")
            session.commit()

    def delete_all(self):
        self._implemented_check()
        with session_factory() as session:
            session.query(self.Model).delete(synchronize_session="fetch")
            session.commit()