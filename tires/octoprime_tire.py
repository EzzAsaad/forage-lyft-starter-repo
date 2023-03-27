from tires import Tire


class OctoprimeTire(Tire):

    def __init__(self, sensors):
        super().__init__(sensors)

    def needs_service(self):
        if sum(self.sensors) >= 3:
            return True
        return False