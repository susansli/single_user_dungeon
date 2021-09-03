from unittest import TestCase
from unittest.mock import patch
import io
from game import heal


class TestHeal(TestCase):
    def test_heal_does_not_exceed_max(self):
        test_character = {"id": 1, "level": 1, "hp": 25}
        heal(test_character)
        expected = 25
        actual = test_character["hp"]
        self.assertEqual(expected, actual)

    def test_heal_when_damaged(self):
        test_character = {"id": 1, "level": 1, "hp": 20}
        heal(test_character)
        expected = 24
        actual = test_character["hp"]
        self.assertEqual(expected, actual)

    def test_heal_higher_level(self):
        test_character = {"id": 1, "level": 2, "hp": 20}
        heal(test_character)
        expected = 25
        actual = test_character["hp"]
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_heal_print(self, mock_output):
        test_character = {"id": 1, "level": 2, "hp": 20}
        heal(test_character)
        expected = "\nYou heal for 5 HP, and currently have 25 HP. Your max HP is 30 HP.\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
