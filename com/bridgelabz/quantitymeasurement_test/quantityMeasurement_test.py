from com.bridgelabz.quantitymeasurement.quantityMeasurement import Feet
from com.bridgelabz.quantitymeasurement.InvalidTypeException import InvalidTypeException
import pytest


def test_givenZeroFeetAndZeroFeet_WhenCompared_ShouldReturnTrue():
    feetValue1 = Feet(0.0)
    feetValue2 = Feet(0.0)
    assert feetValue1 == feetValue2


def test_givenAFeetValue_IfNotFloatType_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        feetValue = Feet(10)


def test_givenTwoSameValues_WhenComparedIfTypeMissMatched_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        feetValue1 = Feet(0.0)
        feetValue2 = float(0.0)
        assert feetValue1 == feetValue2
