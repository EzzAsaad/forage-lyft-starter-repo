from abc import ABC, abstractmethod


class Tire(ABC):
    def __init__(self, sensors):
        super().__init__()
        if len(sensors) != 4:
            raise Exception('there is missing data in sensor data!')

        for sensor in sensors:
            if not(sensor >= 0 and sensor <= 1):
                raise Exception('wrong value in sensors data!')
        self.sensors = sensors

    @abstractmethod
    def needs_service(self):
        pass
    