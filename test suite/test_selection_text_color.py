from unittest import TestCase
from game import selection_text_color


class TestSelectionTextColor(TestCase):
    def test_returned_type(self):
        test_text = selection_text_color("Hello World")
        actual = True
        expected = True
        if not isinstance(test_text, str):
            actual = False
        self.assertEqual(expected, actual)

    def test_quit_string_is_red(self):
        actual = selection_text_color("Quit")
        expected = "\033[31mQuit\033[0m"
        self.assertEqual(expected, actual)

    def test_other_strings_are_blue(self):
        actual = selection_text_color("Hello World")
        expected = "\033[34mHello World\033[0m"
        self.assertEqual(expected, actual)
