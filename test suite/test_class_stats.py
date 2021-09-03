from unittest import TestCase
from unittest.mock import patch
from game import make_character
from game import class_stats


class TestClassStats(TestCase):

    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_returned_type(self, mock_input):
        test_character = make_character()
        test_stats = class_stats(test_character)
        actual = True
        expected = True
        if not isinstance(test_stats, dict):
            actual = False
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_correct_class(self, mock_input):
        test_character = make_character()
        test_stats = class_stats(test_character)
        expected = 'Gunslinger Apprentice'
        actual = test_stats['class_name']
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Susan", "2"])
    def test_correct_stats_at_higher_levels(self, mock_input):
        test_character = make_character()
        test_character['level'] = 2
        test_stats = class_stats(test_character)
        expected = 'Scrapper Adept'
        actual = test_stats['class_name']
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Susan", "3"])
    def test_dictionary_length(self, mock_input):
        test_character = make_character()
        test_stats = class_stats(test_character)
        expected = 10
        actual = len(test_stats)
        self.assertEqual(expected, actual)
