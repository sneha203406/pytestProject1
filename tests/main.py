# This is a sample Python script.
from test_class import TestClass
from test_sample import TestClass1


def main():

    t = TestClass()
    t.test_one()
    t.test_two()

    t = TestClass1()
    t.test_one1()
    t.test_two2()


if __name__ == "__main__":
    main()
