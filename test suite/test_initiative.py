from unittest import TestCase
from unittest.mock import patch
from game import make_character
from game import initiative


class TestInitiative(TestCase):

    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_returned_type(self, mock_input):
        test_character = make_character()
        test_type = initiative(test_character)
        actual = True
        expected = True
        if not isinstance(test_type, str):
            actual = False
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Susan", "4"])
    def test_id_4_always_win(self, mock_input):
        test_character = make_character()
        actual = initiative(test_character)
        expected = "player"
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[50, 1])
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_player_win(self, mock_input, mock_random):
        test_character = make_character()
        actual = initiative(test_character)
        expected = "player"
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 50])
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_mob_win(self, mock_input, mock_random):
        test_character = make_character()
        actual = initiative(test_character)
        expected = "mob"
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 1])
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_draw(self, mock_input, mock_random):
        test_character = make_character()
        actual = initiative(test_character)
        expected = "draw"
        self.assertEqual(expected, actual)
