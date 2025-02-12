from datetime import date
from battery.nubbin_battery import NubbinBattery
from engine.willoughby_engine import WilloughbyEngine
from tires.octoprime_tire import OctoprimeTire
from car import Car


class Rorschach(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, sensors: list):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(sensors=sensors)
        super().__init__(battery=battery, engine=engine, tire=tire)
