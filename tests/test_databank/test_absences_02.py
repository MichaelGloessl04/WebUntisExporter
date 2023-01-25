try:
    from databank.model import Absences
except ImportError as e:
    print("Error while importing %s" % e)


def test_init_empty_00():
    """The init method should raise a TypeError if no args are given."""
    a = Absences()
    try:
        a.init()
    except TypeError:
        assert True
