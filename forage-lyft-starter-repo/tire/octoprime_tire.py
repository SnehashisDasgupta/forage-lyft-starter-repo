from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        sum=0
        for tire in self.tire_wear:
            sum += tire

        if (sum >= 3):
            return True
        else:
            return False


        