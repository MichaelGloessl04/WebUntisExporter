import time


try:
    from databank.model import AbsenceHandler
    from databank.tables import Absences
    from errors import PathError
except ImportError as e:
    print("Error while importing %s" % e)


temp_time = int(time.time())
db_path = "C:/Code/WebUntisExporter/tests/testbase.db"


def test_init_empty_00():
    """The init method should raise a TypeError if no args are given."""
    msg = "AbsenceHandler.__init__() missing 1 required positional argument: 'path'"
    try:
        a = AbsenceHandler()  # noqa: F841
        assert False
    except TypeError as e:
        assert str(e) == msg


def test_init_not_str_01():
    """The init method should raise a TypeError if the input is not a str"""
    wrong_args = [True, 2, 0.0, None]
    for wrong_arg in wrong_args:
        try:
            a = AbsenceHandler(wrong_arg)  # noqa: F841
            assert False
        except TypeError as e:
            msg = ("Path should be <class 'str'>, is %s" %
                   type(wrong_arg))
            assert str(e) == msg


def test_init_path_invalid_02():
    """Test if the given path is valid."""
    wrong_args = ["Robert Ulmer", "", "#:/", "C:/:,#§=", "test:/test.db"]
    for wrong_arg in wrong_args:
        try:
            a = AbsenceHandler(wrong_arg)  # noqa: F841
            assert False
        except PathError as e:
            msg = "'%s' is not a valid path." % wrong_arg
            assert str(e) == msg


def test_init_funcitonality_03():
    """Test if the init method works as intended."""
    a = AbsenceHandler(db_path)  # noqa: F841


def test_Model_04():
    """Test the Model property."""
    a = AbsenceHandler(db_path)  # noqa: F841
    assert a.Model
    assert a.Model == Absences
    try:
        a.Model = ""
        assert False
    except AttributeError:
        assert True


def test_Column_Names_05():
    """Test the Column_Names property."""
    a = AbsenceHandler(db_path)  # noqa: F841
    assert a.Column_Names
    assert a.Column_Names == ["id", "start", "end"]
    try:
        a.Column_Names = ""
        assert False
    except AttributeError:
        assert True


def test_append_06():
    """Test the append method."""
    expected = [(1, temp_time, temp_time)]
    a = AbsenceHandler(db_path)  # noqa: F841
    a.delete_all()
    assert a.append
    a.append(start=temp_time, end=temp_time)

    with a.db_connection.connect() as session:
        result = session.execute("""select * from %s """ % a.Model.__tablename__)
        assert expected == result.fetchall()
        a.delete(column="id", value="1")


def test_delete_07():
    """Test the delete method."""
    expected = []
    a = AbsenceHandler(db_path)  # noqa: F841
    a.delete_all()
    assert a.delete
    a.append(start=temp_time, end=temp_time)
    a.delete("id", "1")

    with a.db_connection.connect() as session:
        result = session.execute("""select * from %s """ % a.Model.__tablename__)
        assert expected == result.fetchall()
        a.delete_all()


def test_delete_all_08():
    """Test the delete_all method."""
    expected = []
    a = AbsenceHandler(db_path)  # noqa: F841
    a.delete_all()
    assert a.delete
    a.append(start=temp_time, end=temp_time)
    a.append(start=temp_time, end=temp_time)
    a.delete_all()

    with a.db_connection.connect() as session:
        result = session.execute("""select * from %s """ % a.Model.__tablename__)
        assert expected == result.fetchall()
        a.delete_all()
