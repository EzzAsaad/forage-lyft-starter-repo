from datetime import date
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery
from car import Car


class Calliope(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        super().__init__(battery=battery, engine=engine)
