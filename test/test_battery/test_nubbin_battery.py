import unittest
from battery.nubbin_battery import NubbinBattery
from datetime import datetime


class TestNubbinBattery(unittest.TestCase):

    def test_nubbin_needs_service_true(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_date = today
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(nubbin_battery.needs_service())

    def test_nubbin_needs_service_false(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_date = today
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(nubbin_battery.needs_service())