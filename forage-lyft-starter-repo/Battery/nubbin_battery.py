
from Battery.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.nubbin_need_service = 4


    def needs_service(self):
        need_service=self.last_service_date.replace(year=self.last_service_date.year+self.nubbin_need_service)

        if need_service<self.current_date:
            return True

        else:
            return False