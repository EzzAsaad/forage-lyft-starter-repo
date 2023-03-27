import unittest
from engine import capulet_engine
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):

    def test_capulet_needs_service_true(self):
        current_mileage = 30001
        last_service_mileage = 0
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet_engine.needs_service())

    def test_capulet_needs_service_false(self):
        current_mileage = 30000
        last_service_mileage = 0
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet_engine.needs_service())