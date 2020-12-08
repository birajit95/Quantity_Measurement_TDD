from com.bridgelabz.quantitymeasurement.quantityMeasurement import Feet
import pytest


def test_givenZeroFeetAndZeroFeet_WhenCompared_ShouldReturnTrue():
    feetValue1 = Feet(0.0)
    feetValue2 = Feet(0.0)
    assert feetValue1 == feetValue2
