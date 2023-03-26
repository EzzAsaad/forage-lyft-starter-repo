import unittest
from datetime import datetime

from requests import session
from car_factory import CarFactory


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, sensors)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        sensors = [0.9,0.2,0.3,0.5]

        car = CarFactory.create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        sensors = [0.8,0.2,0.3,0.5]

        car = CarFactory.create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_glissade(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_glissade(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_glissade(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertFalse(car.needs_service())
    
    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        sensors = [0.9,0.2,0.3,0.5]

        car = CarFactory.create_glissade(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_glissade(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, sensors=sensors)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_palindrome(last_service_date, last_service_date, warning_light_is_on, sensors=sensors)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_palindrome(last_service_date, last_service_date, warning_light_is_on, sensors=sensors)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_palindrome(last_service_date, last_service_date, warning_light_is_on, sensors=sensors)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        sensors = [0.9,0.9,0.9,0.5]

        car = CarFactory.create_palindrome(last_service_date, last_service_date, warning_light_is_on, sensors=sensors)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_palindrome(last_service_date, last_service_date, warning_light_is_on, sensors=sensors)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_rorschach(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_rorschach(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_rorschach(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        sensors = [0.9,0.9,0.9,0.5]

        car = CarFactory.create_rorschach(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_rorschach(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_thovex(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_thovex(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_thovex(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertFalse(car.needs_service())

    def test_tire_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        sensors = [0.9,0.2,0.3,0.5]

        car = CarFactory.create_thovex(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertTrue(car.needs_service())

    def test_tire_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        sensors = [0.1,0.2,0.3,0.5]

        car = CarFactory.create_thovex(last_service_date, last_service_date, current_mileage, last_service_mileage, sensors=sensors)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
