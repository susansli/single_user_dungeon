from unittest import TestCase
from unittest.mock import patch
from game import make_character
from game import move_player


class TestMovePlayer(TestCase):

    @patch('builtins.input', side_effect=["Susan", "1", "5"])
    def test_return_5_if_select_quit(self, mock_input):
        test_character = make_character()
        expected = "5"
        actual = move_player(test_character)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Susan", "1", "2"])
    def test_player_location_is_changed(self, mock_input):
        test_character = make_character()
        move_player(test_character)
        expected = 1
        actual = test_character['x_position']
        self.assertEqual(expected, actual)
