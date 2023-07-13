import unittest

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear = [0.1, 0.9, 1, 0.7]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear = [0.1, 0.8, 0.3, 0.7]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear = [1,1,0,1]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear = [1, 0.8, 0.3, 0.1]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())