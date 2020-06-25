import unittest
from score_management_system import ScoreManagementSystem

class TestScoreManagementSystem(unittest.TestCase):
 
    def test_constructor(self):
        cms = ScoreManagementSystem()
        self.assertIsNotNone(cms)



        def test_read_1(self): #스코어정보
            cms = ScoreManagementSystem()
            self.assertEqual(1, cms.read('score.csv'))

        def test_read_2(self):
            cms = ScoreManagementSystem()
            self.assertEqual(2, cms.read('score.cvs'))





        if __name__ == "__main__":
            unittest.main()