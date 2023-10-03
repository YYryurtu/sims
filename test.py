import unittest
from main1 import*
class a (unittest.TestCase):

    def test_1(self):
        b = Human()
        day = 0
        self.assertTrue(b.live(day=day))

    def test2(self):
        c = Auto()
        self.assertTrue(c.drive())
