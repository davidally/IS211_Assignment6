#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def convertCelsiusToKelvin(a_float):
    K = float(a_float) + 273.15
    return round(K, 2)


def convertCelsiusToFahrenheit(a_float):
    F = (float(a_float) * 1.8) + 32
    return round(F, 2)


def convertFahrenheitToCelsius(a_float):
    C = (float(a_float) - 32) * 0.56
    return round(C, 2)


def convertFahrenheitToKelvin(a_float):
    K = (float(a_float) - 32) * 0.56 + 273.15
    return round(K, 2)


def convertKelvinToCelsius(a_float):
    C = float(a_float) - 273.15
    return round(C, 2)


def convertKelvinToFahrenheit(a_float):
    F = float(a_float) * 1.8 - 459.67
    return round(F, 2)
