from pytest import *

class Test(PyTest):
    def test_init(self):
        """Doc for test_init"""

        # Do stuff here
        raise TestPass("Init")

    def test_terminate(self):
        """Doc for test_terminate"""

        # Do stuff here
        raise TestDone("Terminate")

    def test_1(self):
        """Doc for test_1"""

        # Do stuff here
        raise TestFail("test_1")

    def test_2(self):
        """Doc for test_2"""

        # Do stuff here
        raise TestPass("test_2")

    def test_3(self):
        """Doc for test_2"""

        # Do stuff here
        raise TestPass("test_2")

    def test_4(self):
        """Doc for test_2"""

        # Do stuff here
        raise TestPass("test_2")


if __name__ == '__main__':
	t = Test()
