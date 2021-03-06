# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2015 John Dewey
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import unittest2 as unittest

from aletheia.models.interface import Interface


class TestInterface(unittest.TestCase):
    def setUp(self):
        self._i = Interface()

    def test_has_ipv4_address_attribute_default(self):
        self.assertEquals('ipv4_address', self._i.ipv4_address)

    def test_has_ipv4_gateway_attribute_default(self):
        self.assertEquals('ipv4_gateway', self._i.ipv4_gateway)

    def test_has_ipv4_netmask_attribute_default(self):
        self.assertEquals('ipv4_netmask', self._i.ipv4_netmask)

    def test_has_name_attribute_default(self):
        self.assertEquals('eth0', self._i.name)
