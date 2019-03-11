#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import conversions
import unittest
from decimal import Decimal


class TestConversions(unittest.TestCase):

    def testConvertCelsiusToKelvin(self):
        """Should convert celsius into kelvin.
        """
        result = conversions.convertCelsiusToKelvin(20.0)
        self.assertEqual(result, 293.15)

    def testConvertCelsiusToFahrenheit(self):
        """Should convert celsius into fahrenheit.
        """
        result = conversions.convertCelsiusToFahrenheit(12.4)
        self.assertEqual(result, 54.32)

    def testConvertFahrenheitToCelsius(self):
        result = conversions.convertFahrenheitToCelsius(70.0)
        self.assertEqual(result, 21.11)

    def testConvertFahrenheitToKelvin(self):
        result = conversions.convertFahrenheitToKelvin(70.0)
        self.assertEqual(result, 294.26)

    def testConvertKelvinToCelsius(self):
        result = conversions.convertKelvinToCelsius(200.0)
        self.assertEqual(result, -73.15)

    def testConvertKelvinToFahrenheit(self):
        result = conversions.convertKelvinToFahrenheit(190.09)
        self.assertEqual(result, -117.51)


if __name__ == '__main__':
    unittest.main()
