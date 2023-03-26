from datetime import date
from battery.nubbin_battery import NubbinBattery
from car import Car
from engine.willoughby_engine import WilloughbyEngine


class Rorschach(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        super().__init__(battery=battery, engine=engine)
