def test_import_databank_00():
    try:
        import databank  # noqa: F401
        assert True
    except ModuleNotFoundError:
        assert False


def test_import_model_02():
    try:
        import databank.model  # noqa: F401
        assert True
    except ModuleNotFoundError:
        assert False


def test_import_absences_02():
    try:
        from databank.model import Absences  # noqa: F401
        assert True
    except ModuleNotFoundError:
        assert False


def test_import_subjects_03():
    try:
        from databank.model import Subjects  # noqa: F401
        assert True
    except ModuleNotFoundError:
        assert False


def test_import_teachers_04():
    try:
        from databank.model import Teachers  # noqa: F401
        assert True
    except ModuleNotFoundError:
        assert False


def test_import_todos_05():
    try:
        from databank.model import Todos  # noqa: F401
        assert True
    except ModuleNotFoundError:
        assert False


def test_import_users_06():
    try:
        from databank.model import Users  # noqa: F401
        assert True
    except ModuleNotFoundError:
        assert False
