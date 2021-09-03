from unittest import TestCase
from game import BOSS
from game import check_boss_alive


class TestCheckBossAlive(TestCase):
    def test_check_boss_marked_not_alive(self):
        mob = BOSS()
        check_boss_alive(mob)
        expected = False
        actual = mob["is_alive"]
        self.assertEqual(expected, actual)
