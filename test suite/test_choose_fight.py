from unittest import TestCase
from unittest.mock import patch
from game import choose_fight


class TestChooseFight(TestCase):

    @patch('builtins.input', return_value="1")
    def test_returned_type(self, selection_number):
        test_input = choose_fight()
        actual = True
        expected = True
        if not isinstance(test_input, str):
            actual = False
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="2")
    def test_returned_input_is_correct(self, selection_number):
        expected = "2"
        actual = choose_fight()
        self.assertEqual(expected, actual)
