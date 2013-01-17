import re
import sys
import inspect

class TestPass(Exception):
    pass

class TestFail(Exception):
    pass

class TestDone(Exception):
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
    
