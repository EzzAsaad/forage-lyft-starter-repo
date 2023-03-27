from tires import Tire


class CarriganTire(Tire):

    def __init__(self, sensors):
        super().__init__(sensors)

    def needs_service(self):
        for sensor in self.sensors:
            if sensor >= 0.9:
                return True
        return False