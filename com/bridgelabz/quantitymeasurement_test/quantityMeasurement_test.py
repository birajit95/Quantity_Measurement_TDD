from com.bridgelabz.quantitymeasurement.quantityMeasurement import QuantityMeasurement
from com.bridgelabz.quantitymeasurement.quantityMeasurement import Length
from com.bridgelabz.quantitymeasurement.InvalidTypeException import InvalidTypeException
import pytest


def test_givenZeroFeetAndZeroFeet_WhenCompared_ShouldReturnTrue():
    feetValue1 = QuantityMeasurement(Length.Feet, 0)
    feetValue2 = QuantityMeasurement(Length.Feet, 0)
    assert feetValue1 == feetValue2


def test_givenAValue_IfNotNumberType_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        feetValue1 = QuantityMeasurement(Length.Feet, "ha")
        feetValue2 = QuantityMeasurement(Length.Feet, "h1")
        assert feetValue1 == feetValue2


def test_givenTwoSameValues_WhenComparedIfTypeMissMatched_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        feetValue = QuantityMeasurement(Length.Feet, 0)
        notLengthTypeValue = 0
        assert feetValue == notLengthTypeValue


def test_givenTwoDifferentValuesOfFeetType_WhenCompared_ShouldReturnFalse():
    feetValue1 = QuantityMeasurement(Length.Feet, 2)
    feetValue2 = QuantityMeasurement(Length.Feet, 7)
    assert (feetValue1 == feetValue2) == False


# Test cases for Inch


def test_givenZeroInchAndZeroInch_WhenCompared_ShouldReturnTrue():
    inchValue1 = QuantityMeasurement(Length.Inch, 0)
    inchValue2 = QuantityMeasurement(Length.Inch, 0)
    assert inchValue1 == inchValue2


def test_givenTwoSameInchValues_WhenComparedIfTypeMissMatched_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        inchValue1 = QuantityMeasurement(Length.Inch, 0)
        inchValue2 = float(0.0)
        assert inchValue1 == inchValue2


def test_givenTwoDifferentValuesOfInchType_WhenCompared_ShouldReturnFalse():
    inchValue1 = QuantityMeasurement(Length.Inch, 4)
    inchValue2 = QuantityMeasurement(Length.Inch, 7)
    assert (inchValue1 == inchValue2) == False


# Test Cases for 1 Feet = 12 Inch


def test_given_1FeetAnd_12Inch_WhenCompared_ShouldReturnTrue():
    feetValue = QuantityMeasurement(Length.Feet, 1)
    inchValue = QuantityMeasurement(Length.Inch, 12)
    assert feetValue == inchValue


def test_given_12InchAnd_1Feet_WhenCompared_ShouldReturnTrue():
    inchValue = QuantityMeasurement(Length.Inch,12)
    feetValue = QuantityMeasurement(Length.Feet, 1)
    assert inchValue == feetValue


def test_given_5FeetAnd_60Inch_WhenComapared_ShouldReturnTrue():
    feetValue = QuantityMeasurement(Length.Feet, 5)
    inchValue = QuantityMeasurement(Length.Inch, 60)
    assert feetValue == inchValue


def test_given_60InchAnd_5Feet_WhenComapared_ShouldReturnTrue():
    inchValue = QuantityMeasurement(Length.Inch, 60)
    feetValue = QuantityMeasurement(Length.Feet, 5)
    assert inchValue == feetValue


def test_given_5Inch_60Feet_WhenCompared_ShouldReturnFalse():
    inchValue = QuantityMeasurement(Length.Inch, 5)
    feetValue = QuantityMeasurement(Length.Feet, 60)
    assert (inchValue == feetValue) == False


# Test cases for Yard

def test_givenZeroYardAndZeroYard_WhenCompared_ShouldReturnTrue():
    yardValue1 = QuantityMeasurement(Length.Yard, 0)
    yardValue2 = QuantityMeasurement(Length.Yard, 0)
    assert yardValue1 == yardValue2


def test_givenTwoSameYardValues_WhenComparedIfTypeMissMatched_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        yardValue1 = QuantityMeasurement(Length.Yard, 0)
        yardValue2 = float(0.0)
        assert yardValue1 == yardValue2


def test_givenTwoDifferentValuesOfYardType_WhenCompared_ShouldReturnFalse():
    yardValue1 = QuantityMeasurement(Length.Yard, 14)
    yardValue2 = QuantityMeasurement(Length.Yard, 4)
    assert (yardValue1 == yardValue2) == False


def test_given_3FeetAnd_1Yard_WhenCompared_ShouldReturnTrue():
    assert QuantityMeasurement(Length.Feet,3.0) == QuantityMeasurement(Length.Yard,1.0)


def test_given_1FeetAnd_1Yard_WhenCompared_ShouldReturnFalse():
    assert (QuantityMeasurement(Length.Feet,1.0) == QuantityMeasurement(Length.Yard,1.0)) == False


def test_given_1YardAnd_36Inch_WhenCompared_ShouldReturnTrue():
    assert QuantityMeasurement(Length.Yard,1.0) == QuantityMeasurement(Length.Inch, 36.0)


def test_given_36InchAnd_1Yard_WhenCompared_ShouldReturnTrue():
    assert QuantityMeasurement(Length.Inch, 36.0) == QuantityMeasurement(Length.Yard,1.0)


def test_given_1YardAnd_3Feet_WhenCompared_ShouldReturnTrue():
    assert QuantityMeasurement(Length.Yard,1.0) == QuantityMeasurement(Length.Feet, 3.0)


def test_given_1InchAnd_1Yard_WhenCompared_ShouldReturnFalse():
    assert (QuantityMeasurement(Length.Inch, 1.0) == QuantityMeasurement(Length.Yard, 1.0)) == False


# Test cases for Centimetre

def test_givenZeroCentimetreAndZeroCentimetre_WhenCompared_ShouldReturnTrue():
    assert QuantityMeasurement(Length.Centimetre, 0.0) == QuantityMeasurement(Length.Centimetre, 0)


def test_givenTwoSameCentimetreValues_WhenComparedIfTypeMissMatched_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        assert QuantityMeasurement(Length.Centimetre, 1) == float(1.0)


def test_givenTwoDifferentValuesOfCentimetreType_WhenCompared_ShouldReturnFalse():
    assert (QuantityMeasurement(Length.Centimetre, 2) == QuantityMeasurement(Length.Centimetre, 1)) == False


def test_given_2InchAnd_5Centimetre_WhenCompared_ShouldReturnTrue():
    assert QuantityMeasurement(Length.Inch, 2) == QuantityMeasurement(Length.Centimetre, 5)


def test_given_5CentimetreAnd_2Inch_WhenCompared_ShouldReturnTrue():
    assert QuantityMeasurement(Length.Centimetre, 5) == QuantityMeasurement(Length.Inch, 2)


@pytest.mark.parametrize("length1,length2,expected",
                         [
                             (QuantityMeasurement(Length.Inch, 2), QuantityMeasurement(Length.Feet, 5), False),
                             (QuantityMeasurement(Length.Inch, 2), QuantityMeasurement(Length.Yard, 5), False),
                             (QuantityMeasurement(Length.Centimetre, 5), QuantityMeasurement(Length.Yard, 2), False),
                             (QuantityMeasurement(Length.Centimetre, 5), QuantityMeasurement(Length.Yard, 2), False),

                         ])
def test_given_2InchWithOtherLengthType_WhenCompared_ShouldReturnFalse(length1, length2, expected):
    assert (length1 == length2) == expected

