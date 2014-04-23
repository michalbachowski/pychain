#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import doctest
import pychain.chain

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(pychain.chain, optionflags=doctest.ELLIPSIS))
    return tests
