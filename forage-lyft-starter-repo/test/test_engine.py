import unittest

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_mileage = 0
        engine = CapuletEngine(current_mileage, last_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 29999
        last_mileage = 0
        engine = CapuletEngine(current_mileage, last_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 59999
        last_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_lights_ON = True
        engine = SternmanEngine(warning_lights_ON)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        warning_lights_OFF = False
        engine = SternmanEngine(warning_lights_OFF)
        self.assertTrue(engine.engine_should_be_serviced())