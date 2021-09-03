from unittest import TestCase
from unittest.mock import patch
from game import add_exp
from game import make_mob
from game import BOSS
from game import make_character


class TestAddExp(TestCase):

    @patch('random.randint', return_value=2)
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_exp_increases(self, mock_input, mock_random):
        player = make_character()
        boss = BOSS()
        mob = make_mob(player, boss)
        add_exp(player, mob)
        expected = 25
        actual = player["exp"]
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_boss_exp_no_increase(self, mock_input):
        player = make_character()
        boss = BOSS()
        player["x_position"] = 24
        player["y_position"] = 24
        mob = make_mob(player, boss)
        add_exp(player, mob)
        expected = 0
        actual = player["exp"]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_level_up_properly(self, mock_input, mock_random):
        player = make_character()
        boss = BOSS()
        mob = make_mob(player, boss)
        player["exp"] = 99
        add_exp(player, mob)
        expected = 2
        actual = player["level"]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_level_cap(self, mock_input, mock_random):
        player = make_character()
        boss = BOSS()
        mob = make_mob(player, boss)
        player["exp"] = 250
        player["level"] = 3
        add_exp(player, mob)
        expected = 3
        actual = player["level"]
        self.assertEqual(expected, actual)
