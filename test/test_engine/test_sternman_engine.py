from re import S
import unittest
from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):

    def test_sternman_needs_service_true(self):
        warning_light_is_on = True
        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman_engine.needs_service())

    def test_sternman_needs_service_false(self):
        warning_light_is_on = False
        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman_engine.needs_service())