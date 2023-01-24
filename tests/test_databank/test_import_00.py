def test_import_databank_00():
    """Test if the databank module can be importet."""
    try:
        import databank  # noqa: F401
        assert True
    except ModuleNotFoundError:
        assert False


def test_import_model_02():
    """Test if the model module can be importet."""
    try:
        import databank.model  # noqa: F401
        assert True
    except ModuleNotFoundError:
        assert False


def test_import_absences_02():
    """Test if the absences class can be importet."""
    try:
        from databank.model import Absences  # noqa: F401
        assert True
    except ModuleNotFoundError:
        assert False


def test_import_subjects_03():
    """Test if the subjects class can be importet."""
    try:
        from databank.model import Subjects  # noqa: F401
        assert True
    except ModuleNotFoundError:
        assert False


def test_import_teachers_04():
    """Test if the teacher class can be importet."""
    try:
        from databank.model import Teachers  # noqa: F401
        assert True
    except ModuleNotFoundError:
        assert False


def test_import_todos_05():
    """Test if the todos class can be importet."""
    try:
        from databank.model import Todos  # noqa: F401
        assert True
    except ModuleNotFoundError:
        assert False


def test_import_users_06():
    """Test if the users class can be importet."""
    try:
        from databank.model import Users  # noqa: F401
        assert True
    except ModuleNotFoundError:
        assert False


def test_import_timetable_07():
    """Test if the timetable class can be importet."""
    try:
        from databank.model import Timetable  # noqa: F401
        assert True
    except ModuleNotFoundError:
        assert False
