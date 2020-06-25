import unittest
from score_management_system import ScoreManagementSystem
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open

class TestScoreManagementSystem(unittest.TestCase):
 
    def test_constructor(self):
        cms = ScoreManagementSystem()
        self.assertIsNotNone(cms)



        def test_read_1(self): 
            m_open = mock_open(read_data="1,±è±è±è,90,70,80\n")

            with patch('score_management_ststem.open', m_open):
                 cms = ScoreManagementSystem()
                 self.assertEqual(1, cms.read('score.csv'))

            m_open.assert_called_with('score.csv','rt', encoding="utf-8")


        def test_read_2(self):
            m_open = mock_open(read_data="1,±è±è±è,90,70,80\n2,³ª³ª³ª,80,95,90")

        with patch('car_management_ststem.open', m_open):
            cms = ScoreManagementSystem()
            self.assertEqual(2, cms.read('score.cvs'))


        def test_read_3(self):
            m_open = mock_open(read_data="1,±è±è±è,90,70,80\n2,³ª³ª³ª,80,95,90\n3,´Ù´Ù,80,40,50")

        with patch('car_management_ststem.open', m_open):
            cms = ScoreManagementSystem()
            self.assertEqual(2, cms.read('score.cvs'))




        if __name__ == "__main__":
            unittest.main()