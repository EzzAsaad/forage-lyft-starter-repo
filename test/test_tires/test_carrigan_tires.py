import unittest
from tires.carrigan_tire import CarriganTire


class TestCarriganTires(unittest.TestCase):

    def test_carrigan_needs_service_false(self):
        tier_wear = [0.1, 0.2, 0.3, 0.5]
        tires = CarriganTire(tier_wear)
        self.assertFalse(tires.needs_service())
    
    def test_carrigan_needs_service_true(self):
        tier_wear = [0.9, 0.3, 0.2, 0.5]
        tires = CarriganTire(tier_wear)
        self.assertTrue(tires.needs_service())
