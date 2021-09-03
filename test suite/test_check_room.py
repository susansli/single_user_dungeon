from unittest import TestCase
from unittest.mock import patch
from game import make_board
from game import check_room
import io


class TestCheckRoom(TestCase):

    def test_returned_type(self):
        test_character = {"x_position": 0, "y_position": 0}
        test_board = make_board()
        test_type = check_room(test_board, test_character)
        actual = True
        expected = True
        if not isinstance(test_type, tuple):
            actual = False
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_room_description(self, mock_output):
        test_character = {"x_position": 0, "y_position": 0}
        test_board = make_board()
        check_room(test_board, test_character)
        actual = mock_output.getvalue()
        expected = "\nThis is the stockade. You should get out of here, more guards might be coming...\n"
        self.assertEqual(expected, actual)
