# sample_test.py

import random
try:
    import unittest2 as unittest
except ImportError:
    import unittest

class SampleTest(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        self.fail("shouldn't happen")

    def test_pass(self):
        self.assertEqual(10, 7 + 3)