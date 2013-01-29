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

    def other_function(self):
        """ This function will not run """
        print "You should not see this text"

if __name__ == '__main__':
	Test()
