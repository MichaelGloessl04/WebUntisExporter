import databank


def main():
    t = databank.Teacher()
    t.delete_all()
    t._dump_teacher_names()


if __name__ == "__main__":
    main()
