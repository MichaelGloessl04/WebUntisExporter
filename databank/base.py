import sqlalchemy as db
from .model import Base as base


class Base:
    def __init__(self) -> None:
        self._table_name = ""
        db_connection = db.create_engine("sqlite:///databank/databank.db")
        base.metadata.create_all(db_connection)
        self.session_factory = db.orm.sessionmaker()
        self.session_factory.configure(bind=db_connection)

    @property
    def Table_Name(self):
        if not self._table_name:
            raise NotImplementedError
        return self._table_name

    def delete_id(self, id):
        with self.session_factory() as session:
            stmt = db.delete(self._table_name).where(self.Table_Name == id)
            session.add(stmt)
            session.commit()
