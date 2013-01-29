# Copyright (c) 2012 - 2013, Kristofer Hallin
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the <organization> nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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
        print "\nTest done. %d cases out of %d failed and %d passed." % \
            (self.failed, self.cases, self.passed)

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
        except Exception, e:
            print "Test failed wih unknown error: %s" % e
            self.failed += 1
    
def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def __handle_timeout__(signum, frame):
            raise TestFail("%s timed out after %d seconds" % \
                               (func.__name__, seconds))

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, __handle_timeout__)
            signal.alarm(seconds)
            try:
                func(*args, **kwargs)
            finally:
                signal.alarm(0)
        return wraps(func)(wrapper)
    return decorator
