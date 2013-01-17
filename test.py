from pytest import *

class Test(PyTest):
    def test_init(self):
        # Do stuff here
        raise TestPass("Init")

    def test_terminate(self):
        # Do stuff here
        raise TestDone("Terminate")

    def test_1(self):
        # Do stuff here
        raise TestFail("test_1")

    def test_2(self):
        # Do stuff here
        raise TestPass("test_2")

    def test_3(self):
        # Do stuff here
        raise TestPass("test_3")

    def test_4(self):
        # Do stuff here
        raise TestPass("test_4")


if __name__ == '__main__':
	Test()
