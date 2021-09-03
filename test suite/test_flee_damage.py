from unittest import TestCase
from unittest.mock import patch
from game import make_character
from game import flee_damage


class TestFleeDamage(TestCase):

    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_cannot_flee_from_boss(self, mock_input):
        test_character = make_character()
        test_character["x_position"] = 24
        test_character["y_position"] = 24
        test_character["in_combat"] = True
        flee_damage(test_character)
        expected = True
        actual = test_character["in_combat"]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_remove_from_combat_after_flee(self, mock_input, mock_random):
        test_character = make_character()
        test_character["in_combat"] = True
        flee_damage(test_character)
        expected = False
        actual = test_character["in_combat"]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_no_damage_after_flee(self, mock_input, mock_random):
        test_character = make_character()
        flee_damage(test_character)
        expected = 25
        actual = test_character["hp"]
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[1, 1])
    @patch('builtins.input', side_effect=["Susan", "1"])
    def test_take_damage_after_flee(self, mock_input, mock_random):
        test_character = make_character()
        flee_damage(test_character)
        expected = 24
        actual = test_character["hp"]
        self.assertEqual(expected, actual)
