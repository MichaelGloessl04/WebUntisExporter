try:
    from databank.model import Absences
    from errors import PathError
except ImportError as e:
    print("Error while importing %s" % e)


def test_init_empty_00():
    """The init method should raise a TypeError if no args are given."""
    a = Absences()
    msg = "BaseModel.init() missing 1 required positional argument: 'path'"
    try:
        a.init()
    except TypeError as e:
        assert str(e) == msg


def test_init_not_str_01():
    """The init method should raise a TypeError if the input is not a str"""
    a = Absences()
    wrong_args = [True, 2, 0.0, None]
    for wrong_arg in wrong_args:
        try:
            a.init(wrong_arg)
        except TypeError as e:
            msg = ("Path should be <class 'str'>, is %s" %
                   type(wrong_arg))
            assert str(e) == msg


def test_init_path_invalid_02():
    """Test if the given path is valid."""
    a = Absences()
    wrong_args = ["Robert Ulmer", "", "#:/", "C:/:,#§=", "test:/test.db"]
    for wrong_arg in wrong_args:
        try:
            a.init(wrong_arg)
            assert False
        except PathError as e:
            msg = "'%s' is not a valid path." % wrong_arg
            assert str(e) == msg


def test_init_funcitonality_03():
    """Test if the init method works as intended."""
    a = Absences()
    a.init("C:/Code/WebUntisExporter/tests/testbase.db")


def test_Model_04():
    """Test the Model property."""
    a = Absences()
    assert a.Model
    assert a.Model == Absences
    try:
        a.Model = ""
        assert False
    except AttributeError:
        assert True

def test_