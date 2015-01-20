#!/usr/bin/env python
""" Tests for pycazy module

test_getfamily.py

(c) The James Hutton Institute 2014
Author: Leighton Pritchard

Contact:
leighton.pritchard@hutton.ac.uk

Leighton Pritchard,
Information and Computing Sciences,
James Hutton Institute,
Errol Road,
Invergowrie,
Dundee,
DD6 9LH,
Scotland,
UK

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Builtins
import os
import requests
import unittest

# Do we have BeautifulSoup4
try:
    from bs4 import BeautifulSoup
except ImportError:
    raise MissingPythonDependencyError(
            "Install BeautifulSoup4 if you want to use pyCAZy.")

# pyCAZy import
import pycazy

# Test ability to get all sequence info for a CAZy family
class GetClassSeqTest(unittest.TestCase):
    def test_get_all_family_seqinfo(self):
        """ Get all sequence info for a single CAZy family.
        """
        seqinfo = pycazy.get_family_seqinfo('GH1', filter='all')

# Run tests
if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
