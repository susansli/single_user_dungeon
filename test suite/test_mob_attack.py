from unittest import TestCase
from unittest.mock import patch
from game import make_character
from game import mob_attack
from game import ENEMY_L1


class TestMobAttack(TestCase):

    @patch('random.randint', return_value=1)
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_mob_flee(self, mock_input, mock_random):
        test_character = make_character()
        test_mob = ENEMY_L1()
        mob_attack(test_character, test_mob)
        expected_combat_state = False
        actual_combat_state = test_character["in_combat"]
        expected_hp = 25
        actual_hp = test_character["hp"]
        self.assertEqual(expected_combat_state, actual_combat_state)
        self.assertEqual(expected_hp, actual_hp)

    @patch('random.randint', return_value=3)
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_player_takes_damage(self, mock_input, mock_random):
        test_character = make_character()
        test_mob = ENEMY_L1()
        mob_attack(test_character, test_mob)
        expected = 22
        actual = test_character["hp"]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=7)
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_attack_miss(self, mock_input, mock_random):
        test_character = make_character()
        test_mob = ENEMY_L1()
        mob_attack(test_character, test_mob)
        expected = 25
        actual = test_character["hp"]
        self.assertEqual(expected, actual)
