from datetime import date
from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery
from tires.octoprime_tire import OctoprimeTire
from car import Car

class Palindrome(Car):
    def __init__(self, current_date: date, last_service_date: date, waring_light_is_on: bool, sensors: list):
        engine = SternmanEngine(waring_light_is_on)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(sensors=sensors)
        super().__init__(battery=battery, engine=engine, tire=tire)
