import unittest
from tires.octoprime_tire import OctoprimeTire


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_false(self):
        tier_wear = [0.1, 0.2, 0.3, 0.5]
        tires = OctoprimeTire(tier_wear)
        self.assertFalse(tires.needs_service())

    def test_needs_service_true(self):
        tier_wear = [0.9, 0.9, 0.9, 0.5]
        tires = OctoprimeTire(tier_wear)
        self.assertTrue(tires.needs_service())
    