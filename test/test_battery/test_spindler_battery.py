import unittest
from battery.spindler_battery import SpindlerBattery
from datetime import datetime


class TestSpindlerBattery(unittest.TestCase):

    def test_spindler_needs_service_true(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_date = today
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spindler_battery.needs_service())

    def test_spindler_needs_service_false(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_date = today
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(spindler_battery.needs_service())