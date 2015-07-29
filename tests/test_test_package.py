#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_test_package
----------------------------------

Tests for `test_package` module.
"""

import unittest

from test_package import test_package


class TestTest_package(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        c = test_package.foo(4, 7)
        assert c == 11

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
