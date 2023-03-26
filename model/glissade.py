from datetime import date
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from tire.carrigan_tire import CarriganTire
from car import Car


class Glissade(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, sensors: list):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(sensors=sensors)
        super().__init__(battery=battery, engine=engine, tire=tire)
