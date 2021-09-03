from unittest import TestCase
from game import make_board


class TestMakeBoard(TestCase):

    def test_returned_type(self):
        test_board = make_board()
        actual = True
        expected = True
        if not isinstance(test_board, dict):
            actual = False
        self.assertEqual(expected, actual)

    def test_dictionary_length(self):
        test_board = make_board()
        expected = 625
        actual = len(test_board)
        self.assertEqual(expected, actual)

    def test_stockade_area_description(self):
        test_board = make_board()
        actual = True
        expected = True
        for key, value in test_board.items():
            x, y = key
            if x in range(5) and y in range(5):
                if test_board[key] != "This is the stockade. You should get out of here, more guards might be coming" \
                                      "...":
                    actual = False
        self.assertEqual(expected, actual)

    def test_library_area_description(self):
        test_board = make_board()
        actual = True
        expected = True
        for key, value in test_board.items():
            x, y = key
            if x in range(10) and y in range(10, 15):
                if test_board[key] != "Thousands of books line the walls, and you can’t help but admire them. " \
                                      "A wealth of\ninformation like this, in the middle of this godforsaken place...":
                    actual = False
        self.assertEqual(expected, actual)

    def test_shrine_area_description(self):
        test_board = make_board()
        actual = True
        expected = True
        for key, value in test_board.items():
            x, y = key
            if x in range(16, 25) and y in range(0, 5):
                if test_board[key] != "Beautiful stained glass windows send light bouncing around the room, a visual " \
                           "cornucopia.\nThis must be a shrine of some sort...":
                    actual = False
        self.assertEqual(expected, actual)

    def test_final_area_description(self):
        test_board = make_board()
        actual = True
        expected = True
        for key, value in test_board.items():
            x, y = key
            if x in range(20, 25) and y in range(20, 25):
                if (x, y) != (24, 24):
                    if test_board[key] != "You sense that you are close to the exit, however you see a man in the " \
                                          "distance… his eyes\n pass over you, even though you are out of his line " \
                                          "of sight. You feel like you are being watched.":
                        actual = False
        self.assertEqual(expected, actual)

    def test_boss_battle_description(self):
        test_board = make_board()
        actual = True
        expected = True
        for key, value in test_board.items():
            if key == (24, 24):
                if test_board[key] != "This is the final room. You see that man walking towards you, a hideous grin " \
                                      "on his face.\nYou prepare yourself for a tough fight.":
                    actual = False
        self.assertEqual(expected, actual)

    def test_other_room_description_valid(self):
        test_board = make_board()
        actual = True
        expected = True
        for key, value in test_board.items():
            x, y = key
            if (x not in range(5) and y not in range(5)) \
                    and (x not in range(10) and y not in range(10, 15)) \
                    and (x not in range(16, 25) and y not in range(0, 5)) \
                    and (x not in range(20, 25) and y not in range(20, 55)) \
                    and ((x, y) != (24, 24)):
                if test_board[key] not in ["The air smells like must and ancient things long forgotten...",
                                           "Your steps echo ominously off the stone walls...",
                                           "Shadows dance on the dark walls, like raindrops on top of snow...",
                                           "A strange but haunting hymn echoes around you..."]:
                    actual = False
        self.assertEqual(expected, actual)
