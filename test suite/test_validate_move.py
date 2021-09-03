from unittest import TestCase
from game import validate_move


class TestValidateMove(TestCase):
    def test_returned_type(self):
        test_type = validate_move("1", (0, 0))
        actual = True
        expected = True
        if not isinstance(test_type, bool):
            actual = False
        self.assertEqual(expected, actual)

    def test_invalid_move(self):
        actual = validate_move("1", (0, 0))
        expected = False
        self.assertEqual(expected, actual)

    def test_valid_move(self):
        actual = validate_move("2", (0, 0))
        expected = True
        self.assertEqual(expected, actual)
