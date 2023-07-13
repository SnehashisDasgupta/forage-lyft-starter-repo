import unittest
import datetime

from Battery.nubbin_battery import NubbinBattery
from Battery.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date= datetime.datetime(2023,6,3)
        last_service_date=datetime.datetime(2018,1,22)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.datetime(2023,6,3)
        last_service_date = datetime.datetime(2021,6,4)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date= datetime.datetime(2023,6,3)
        last_service_date=datetime.datetime(2020,12,20)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.datetime(2023,6,3)
        last_service_date = datetime.datetime(2019,8,24)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())