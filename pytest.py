import os
import re
import sys
import errno
import signal
import inspect

from functools import wraps

class TestPass(Exception):
    pass

class TestFail(Exception):
    pass

class TestDone(Exception):
    pass

class TestTimeout(Exception):
    pass

class PyTest():
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.cases = 0
        functions = inspect.getmembers(self)
        self.run_test(self.test_init)
        for func, obj in functions:
            if not re.search("test_[0-9]+", func):
                continue
            self.run_test(obj)
        self.run_test(self.test_terminate)

    def run_test(self, test):
        try:    
            if test.__doc__ != None:
                print test.__doc__
            self.cases += 1
            test()
        except TestPass, e:
            print "Test PASSED: %s" % e
            self.passed += 1
        except TestFail, e:
            print "Test FAILED: %s" % e
            self.failed += 1
        except TestDone, e:
            self.passed += 1
            print "\nTest done. %d cases out of %d failed and %d passed." % \
                (self.failed, self.cases, self.passed)
        except Exception, e:
            print "Test failed wih unknown error: %s" % e
            self.failed += 1
    
def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def __handle_timeout__(signum, frame):
            raise TestTimeout(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, __handle_timeout__)
            signal.alarm(seconds)
            try:
                func(*args, **kwargs)
            finally:
                signal.alarm(0)
                raise TestFail("%s timed out after %d seconds" % (func.__name__, seconds))
        return wraps(func)(wrapper)
    return decorator
