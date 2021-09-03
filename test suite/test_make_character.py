from unittest import TestCase
from unittest.mock import patch
from game import make_character


class TestMakeCharacter(TestCase):

    @patch('builtins.input', side_effect=["Susan", "2"])
    def test_name_is_correct(self, mock_input):
        test_dictionary = make_character()
        expected = '\x1b[32mSusan\x1b[0m'
        actual = test_dictionary['name']
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_return_dictionary_is_correct(self, mock_input):
        expected = {'name': '\x1b[32mSusan\x1b[0m', 'hp': 25, 'class_name': 'Gunslinger Apprentice', 'id': 1,
                    'level': 1, 'exp': 0, 'x_position': 0, 'y_position': 0, 'in_combat': False, 'is_alive': True}
        actual = make_character()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Susan", "3"])
    def test_returned_type(self, mock_input):
        test_type = make_character()
        actual = True
        expected = True
        if not isinstance(test_type, dict):
            actual = False
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Susan", "3"])
    def test_dictionary_correct_length(self, mock_input):
        test_dictionary = make_character()
        expected = 10
        actual = len(test_dictionary)
        self.assertEqual(expected, actual)
