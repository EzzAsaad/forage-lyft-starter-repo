from car import Car
from datetime import date
from model.calliope import Calliope
from model.glissade import Glissade
from model.rorschach import Rorschach
from model.thovex import Thovex
from model.palindrome import Palindrome


class CarFactory(Car):
    def create_calliope(self,current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Calliope(current_date=current_date, last_service_date=last_service_date, current_mileage=current_mileage,last_service_mileage=last_service_mileage)
    def create_glissade(self,current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Glissade(current_date=current_date, last_service_date=last_service_date, current_mileage=current_mileage,last_service_mileage=last_service_mileage)
    def create_rorschach(self,current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Rorschach(current_date=current_date, last_service_date=last_service_date, current_mileage=current_mileage,last_service_mileage=last_service_mileage)
    def create_thovex(self,current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Thovex(current_date=current_date, last_service_date=last_service_date, current_mileage=current_mileage,last_service_mileage=last_service_mileage)
    def create_palindrome(self,current_date: date, last_service_date: date, waring_light_is_on: bool):
        return Palindrome(current_date=current_date, last_service_date=last_service_date, waring_light_is_on=waring_light_is_on)
    
