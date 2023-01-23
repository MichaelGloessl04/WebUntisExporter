import databank.model as models


def main():
    t = models.Teachers()
    t.delete_all()


if __name__ == "__main__":
    main()
