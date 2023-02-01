import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
import os
from errors import PathError


Base = declarative_base()


class BaseModel:
    """An abstract base class for the database models.

    Args:


    Raises:
        NotImplementedError: If the BaseModel class is directily declared as
                             an object the error gets raised.

    Returns:
        None: returns nothing
    """

    def __init__(self, path: str) -> None:
        """Initializes needed values and access the path of the database."""
        self._implemented_check()
        self._table = None
        if type(path) is not str:
            raise TypeError("Path should be <class 'str'>, is %s" %
                            type(path))
        path = self._validate_path(path)
        self._db_connection = db.create_engine("sqlite:///" + path)
        Base.metadata.create_all(bind=self._db_connection)
        self.session_factory = db.orm.sessionmaker()
        self.session_factory.configure(bind=self._db_connection)

    @property
    def Model(self):
        """Return the type of the current object.

        Returns:
            BaseModel: The current Model.
        """
        self._implemented_check()
        return self._table

    @property
    def Table_Name(self):
        """Return the name of the current table.

        Returns:
            str: String containing name of current table.
        """
        return self._table.name

    @property
    def Column_Names(self):
        """Return the name of all collumns in the current model.

        Returns:
            list: a list of strings with all collumn names
        """
        self._implemented_check()  # test
        columns = self.Model.c
        return [c.name for c in columns]

    def _implemented_check(self):
        if type(self) == BaseModel:
            raise NotImplementedError

    def _validate_path(self, path):
        return_path = os.path.normpath(path)
        temp_path = path
        if temp_path.find(".db") <= 0:  # If path has no .db ending raise error
            raise PathError("'%s' is not a valid path." % path)
        while True:  # remove file from path
            if temp_path[-1].find('/') == 0:
                break
            temp_path = temp_path[:-1]
        if not os.path.exists(temp_path):  # If path doesnt exist raise error
            raise PathError("'%s' is not a valid path." % path)
        return return_path

    def _is_valid_type(self, value, *types):
        pass  # TODO: Implement

    def append(self, **collumns):
        """Adds an entry to the the current Model."""
        self._implemented_check()
        with self.session_factory() as session:
            entry = self.Model(**collumns)
            session.add(entry)
            session.commit()

    def delete(self, column: str, value: any):
        """Deletes entries based on the given column and value."""
        self._implemented_check()
        with self.session_factory() as session:
            session.query(self.Model).filter(
                getattr(self.Model, column) == value
                ).delete(synchronize_session="fetch")
            session.commit()

    def delete_all(self):
        """Deletes all entries."""
        self._implemented_check()
        with self.session_factory() as session:
            session.query(self.Model).delete(synchronize_session="fetch")
            session.commit()
