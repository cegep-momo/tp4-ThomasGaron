import unittest
from gpiozero import Device, Button
from gpiozero.pins.mock import MockFactory

from view.platine import Platine

Device.pin_factory = MockFactory()

class TestPlatine(unittest.TestCase):
    def setUp(self):
        self.platine = Platine()

    def test_bouton_presse(self):
        self.platine.bouton_Start.pin.drive_low()
        self.assertTrue(self.platine.bouton_Start.is_active)

    def test_bouton_relache(self):
        self.platine.bouton_Start.pin.drive_high()
        self.assertFalse(self.platine.bouton_Start.is_active)

if __name__ == '__main__':
    unittest.main()