try:
    from databank.model import BaseModel
except ImportError as e:
    print("Error while importing %s" % e)


def test_init_00():
    """Test if the init method raises the expected exception."""
    try:
        bm = BaseModel("C:/Code/WebUntisExporter/tests/testbase.db")
        bm.Model
        assert False
    except NotImplementedError:
        assert True


def test_model_01():
    """Test if the Model property raises the expected exception."""
    try:
        bm = BaseModel("C:/Code/WebUntisExporter/tests/testbase.db")
        bm.Model
        assert False
    except NotImplementedError:
        assert True


def test_column_names_02():
    """Test if the Column_Names property raises the expected exception."""
    try:
        bm = BaseModel("C:/Code/WebUntisExporter/tests/testbase.db")
        bm.Column_Names
        assert False
    except NotImplementedError:
        assert True


def test_append_03():
    """Test if the append method raises the expected exception."""
    try:
        bm = BaseModel("C:/Code/WebUntisExporter/tests/testbase.db")
        bm.append(id=0, short_name="TS", long_name="test")
        assert False
    except NotImplementedError:
        assert True


def test_delete_04():
    """Test if the delete method raises the expected exception."""
    try:
        bm = BaseModel("C:/Code/WebUntisExporter/tests/testbase.db")
        bm.delete("id", 0)
        assert False
    except NotImplementedError:
        assert True


def test_delete_all_05():
    """Test if the delete_all method raises the expected exception."""
    try:
        bm = BaseModel("C:/Code/WebUntisExporter/tests/testbase.db")
        bm.delete_all()
        assert False
    except NotImplementedError:
        assert True
