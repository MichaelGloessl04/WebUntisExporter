try:
    from databank.model import AbsenceHandler
    from databank.tables import Absences
    from errors import PathError
except ImportError as e:
    print("Error while importing %s" % e)


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
    a = AbsenceHandler("C:/Code/WebUntisExporter/tests/testbase.db")  # noqa: F841


def test_Model_04():
    """Test the Model property."""
    a = AbsenceHandler("C:/Code/WebUntisExporter/tests/testbase.db")  # noqa: F841
    assert a.Model
    assert a.Model == Absences
    try:
        a.Model = ""
        assert False
    except AttributeError:
        assert True


def test_Column_Names_05():
    """Test the Column_Names property."""
    a = AbsenceHandler("C:/Code/WebUntisExporter/tests/testbase.db")  # noqa: F841
    assert a.Column_Names
    assert a.Column_Names == ["id", "start", "end"]
    try:
        a.Column_Names = ""
        assert False
    except AttributeError:
        assert True
