from unittest import TestCase
from unittest.mock import patch
from game import check_combat


class TestCheckCombat(TestCase):

    def test_boss_always_initiates_combat(self):
        test_character = {"x_position": 24, "y_position": 24, "in_combat": False}
        check_combat(test_character)
        expected = True
        actual = test_character["in_combat"]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_combat_false(self, mock_random):
        test_character = {"x_position": 5, "y_position": 10, "in_combat": False}
        check_combat(test_character)
        expected = False
        actual = test_character["in_combat"]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_combat_true(self, mock_random):
        test_character = {"x_position": 5, "y_position": 10, "in_combat": False}
        check_combat(test_character)
        expected = True
        actual = test_character["in_combat"]
        self.assertEqual(expected, actual)
