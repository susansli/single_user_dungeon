from unittest import TestCase
from unittest.mock import patch
from game import make_character
from game import get_user_choice


class TestGetUserChoice(TestCase):

    @patch('builtins.input', side_effect=["Susan", "1", "1"])
    def test_returned_type(self, selection_number):
        test_character = make_character()
        test_input = get_user_choice(test_character)
        actual = True
        expected = True
        if not isinstance(test_input, str):
            actual = False
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Susan", "1", "4"])
    def test_input_correct(self, selection_number):
        test_character = make_character()
        actual = get_user_choice(test_character)
        expected = "4"
        self.assertEqual(expected, actual)
