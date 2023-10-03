import unittest
from main1 import*
class a (unittest.TestCase):

    def test_1(self):
        b = Human()
        day = 0
        self.assertTrue(b.live(day=day))
        self.assertTrue(b.shopping())
        self.assertTrue(b.work())
        self.assertTrue(b.eat())
        self.assertTrue(b.get_job())
        self.assertTrue(b.is_alive())
        self.assertTrue(b.live())




    def test2(self):
        c = Auto()
        self.assertTrue(c.drive())
