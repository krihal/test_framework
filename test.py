from time import sleep
from pytest import *

class Test(PyTest):
    def test_init(self):
        """ This test case will always run first """
        # Do stuff here
        raise TestPass("Init")

    def test_terminate(self):
        """ This test case will always run last """
        # Do stuff here
        raise TestPass("Terminate")

    def test_1(self):
        """ This test case will fail """
        # Do stuff here
        raise TestFail("test_1")

    def test_2(self):
        """ This test case will pass """
        # Do stuff here
        raise TestPass("test_2")

    def test_3(self):
        """ This is just a random text """
        # Do stuff here
        raise TestPass("test_3")

    # This case will time out after 2 seconds
    @timeout(2)
    def test_4(self):
        """ This function will time out after 2 seconds..."""
        sleep(10)
        raise TestPass("test_4")


if __name__ == '__main__':
	Test()
