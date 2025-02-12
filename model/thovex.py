from datetime import date
from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from tires.carrigan_tire import CarriganTire
from car import Car


class Thovex(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, sensors: list):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(sensors=sensors)
        super().__init__(battery=battery, engine=engine, tire=tire)
