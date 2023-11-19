import unittest
import Poker

class Test_Poker(unittest.TestCase):
    def test_straight(self):
        self.assertTrue(Poker.straight([28,29,30,31,32]))

    def test_full_house(self):
        self.assertTrue(Poker.full_house([2,2,3,3,3]))

    def test_straight_flush(self):
        self.assertTrue(Poker.straight_flush([1,2,3,4,5]))

if __name__ == "__main__":
    unittest.main()