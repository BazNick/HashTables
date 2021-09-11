import unittest

from Main import create, search, remove


class TestHashMap(unittest.TestCase):
    def test_create(self):
        self.assertEqual(create(), 10)

    def test_search(self):
        self.assertTrue(search)

    def test_remove(self):
        self.assertFalse(remove())
