import unittest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ej14 import ConversorTemperatura


class ConversorTemperaturaTest(unittest.TestCase):

    def test_celsius_a_fahrenheit_100(self):
        self.assertEqual(ConversorTemperatura.celsius_a_fahrenheit(100), 212.0)

    def test_celsius_a_fahrenheit_0(self):
        self.assertEqual(ConversorTemperatura.celsius_a_fahrenheit(0), 32.0)

    def test_fahrenheit_a_celsius_32(self):
        self.assertEqual(ConversorTemperatura.fahrenheit_a_celsius(32), 0.0)

    def test_celsius_a_kelvin_0(self):
        self.assertAlmostEqual(ConversorTemperatura.celsius_a_kelvin(0), 273.15, places=2)

    def test_kelvin_negativo(self):
        with self.assertRaises(ValueError):
            ConversorTemperatura.kelvin_a_celsius(-10)

    def test_cero_absoluto(self):
        self.assertAlmostEqual(ConversorTemperatura.celsius_a_kelvin(-273.15), 0.0, places=2)


if __name__ == '__main__':
    unittest.main()
