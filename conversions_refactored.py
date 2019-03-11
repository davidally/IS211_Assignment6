#!/usr/bin/env python2
# -*- coding: utf-8 -*-


class CatchFaultyConversion(Exception):
    pass


def convert(fromUnit, toUnit, val):

    if fromUnit.lower() == "celsius" and toUnit.lower() == "kelvin":
        return float(val) + 273.15

    elif fromUnit.lower() == "celsius" and toUnit.lower() == "fahrenheit":
        return float(val) * 9 / 5 + 32

    elif fromUnit.lower() == "fahrenheit" and toUnit.lower() == "celsius":
        return (float(val) - 32) * 5 / 9

    elif fromUnit.lower() == "fahrenheit" and toUnit.lower() == "kelvin":
        return (float(val) + 459.67) * 5 / 9

    elif fromUnit.lower() == "kelvin" and toUnit.lower() == "fahrenheit":
        return float(val) * 9 / 5 - 459.67

    elif fromUnit.lower() == "kelvin" and toUnit.lower() == "celsius":
        return float(val) - 273.15

    elif fromUnit.lower() == "yards" and toUnit.lower() == "miles":
        return float(val) / 1760

    elif fromUnit.lower() == "yards" and toUnit.lower() == "meters":
        return float(val) / 1.094

    elif fromUnit.lower() == "meters" and toUnit.lower() == "yards":
        return float(val) * 1.094

    elif fromUnit.lower() == "meters" and toUnit.lower() == "miles":
        return float(val) / 1609.344

    elif fromUnit.lower() == "miles" and toUnit.lower() == "yards":
        return float(val) * 1760

    elif fromUnit.lower() == "miles" and toUnit.lower() == "meters":
        return float(val) * 1609.344

    elif fromUnit.lower() == toUnit.lower():
        return val

    else:
        raise CatchFaultyConversion("Input is invalid please try again.")
