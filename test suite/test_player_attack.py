from unittest import TestCase
from unittest.mock import patch
from game import make_character
from game import player_attack
from game import ENEMY_L1


class TestPlayerAttack(TestCase):

    @patch('random.randint', side_effect=[5, 1, 1])
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_enemy_takes_damage(self, mock_input, mock_random):
        test_character = make_character()
        test_mob = ENEMY_L1()
        player_attack(test_character, test_mob)
        expected = 10
        actual = test_mob["hp"]
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[5, 10, 1])
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_attack_miss(self, mock_input, mock_random):
        test_character = make_character()
        test_mob = ENEMY_L1()
        player_attack(test_character, test_mob)
        expected = 15
        actual = test_mob["hp"]
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[4, 1, 1, 1])
    @patch('builtins.input', side_effect=["Susan", "2"])
    def test_attack_crit(self, mock_input, mock_random):
        test_character = make_character()
        test_mob = ENEMY_L1()
        player_attack(test_character, test_mob)
        expected = 10
        actual = test_mob["hp"]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_gunslinger_never_crit(self, mock_input, mock_random):
        test_character = make_character()
        test_mob = ENEMY_L1()
        player_attack(test_character, test_mob)
        expected = 14
        actual = test_mob["hp"]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=10)
    @patch('builtins.input', side_effect=["Susan", "4"])
    def test_rogue_never_miss(self, mock_input, mock_random):
        test_character = make_character()
        test_mob = ENEMY_L1()
        player_attack(test_character, test_mob)
        expected = 5
        actual = test_mob["hp"]
        self.assertEqual(expected, actual)
