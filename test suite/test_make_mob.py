from unittest import TestCase
from unittest.mock import patch
from game import BOSS
from game import ENEMY_STOCKADE
from game import ENEMY_LIBRARY
from game import ENEMY_L2
from game import ENEMY_L3
from game import make_character
from game import make_mob


class TestMakeMob(TestCase):

    @patch('random.randint', return_value=7)
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_stockade_area(self, mock_input, mock_random):
        test_character = make_character()
        test_character["x_position"] = 10
        test_character["y_position"] = 10
        actual = make_mob(test_character, BOSS())
        expected = ENEMY_L2()
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=5)
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_stockade_area(self, mock_input, mock_random):
        test_character = make_character()
        actual = make_mob(test_character, BOSS())
        expected = ENEMY_STOCKADE()
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=10)
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_library_area(self, mock_input, mock_random):
        test_character = make_character()
        test_character["x_position"] = 5
        test_character["y_position"] = 11
        actual = make_mob(test_character, BOSS())
        expected = ENEMY_LIBRARY()
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=7)
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_shrine_area(self, mock_input, mock_random):
        test_character = make_character()
        test_character["x_position"] = 17
        test_character["y_position"] = 4
        actual = make_mob(test_character, BOSS())
        expected = ENEMY_L2()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_final_area(self, mock_input):
        test_character = make_character()
        test_character["x_position"] = 23
        test_character["y_position"] = 23
        actual = make_mob(test_character, BOSS())
        expected = ENEMY_L3()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_boss_room(self, mock_input):
        test_character = make_character()
        test_character["x_position"] = 24
        test_character["y_position"] = 24
        actual = make_mob(test_character, BOSS())
        expected = BOSS()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_returned_type(self, mock_input):
        test_character = make_character()
        test_type = make_mob(test_character, BOSS())
        actual = True
        expected = True
        if not isinstance(test_type, dict):
            actual = False
        self.assertEqual(expected, actual)
