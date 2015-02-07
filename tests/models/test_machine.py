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

from aletheia.models.machine import Machine


class TestMachine(unittest.TestCase):
    def setUp(self):
        self._m = Machine()

    def test_has_cobbler_attribute_default(self):
        self.assertEquals('cobbler', self._m.cobbler)

    def test_has_domain_attribute_default(self):
        self.assertEquals('domain', self._m.domain)

    def test_has_interfaces_attribute_default(self):
        self.assertEquals(['interface'], self._m.interfaces)

    def test_has_hostname_attribute_default(self):
        self.assertEquals('hostname', self._m.hostname)

    def test_has_mac_address_attribute_default(self):
        self.assertEquals('mac', self._m.mac_address)

    def test_has_management_attribute_default(self):
        self.assertEquals('management', self._m.management)

    def test_has_name_attribute_default(self):
        self.assertEquals('name', self._m.name)

    def test_has_role_attribute_default(self):
        self.assertEquals('role', self._m.role)

    def test_has_type_attribute_default(self):
        self.assertEquals('type', self._m.type)
