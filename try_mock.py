import unittest
from unittest.mock import patch
# import getrandom
from getrandom import get_random_plus_one

class TestRandom(unittest.TestCase):


    @patch('getrandom.random.randint')
    def test_it_shold_call_rannint_with_1_and_10(self, mock):
        get_random_plus_one()
        mock.assert_called_once_with(1,10)
        ## assert here

    @patch('getrandom.random.randint') # mock ไหน patch ไปตรงที่เรียก
    def test_it_shold_get_4_with_readom_get_3(self, mock):
        mock.return_value = 3
        result = get_random_plus_one()
        self.assertEqual(result, 4)

    def test_it_should_get_3(self):
        while True:
            result = get_random_plus_one()
            if result == 3 :
                break
        self.assertEqual(result, 3)

unittest.main()