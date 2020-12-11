from com.bridgelabz.quantitymeasurement.quantityMeasurement import QuantityMeasurement
from com.bridgelabz.quantitymeasurement.Unit import Unit
from com.bridgelabz.quantitymeasurement.InvalidTypeException import InvalidTypeException
import pytest


def test_givenZeroFeetAndZeroFeet_WhenCompared_ShouldReturnTrue():
    feetValue1 = QuantityMeasurement(Unit.Feet, 0)
    feetValue2 = QuantityMeasurement(Unit.Feet, 0)
    assert feetValue1 == feetValue2


def test_givenAValue_IfNotNumberType_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        feetValue1 = QuantityMeasurement(Unit.Feet, "ha")
        feetValue2 = QuantityMeasurement(Unit.Feet, "h1")
        assert feetValue1 == feetValue2


def test_givenTwoSameValues_WhenComparedIfTypeMissMatched_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        feetValue = QuantityMeasurement(Unit.Feet, 0)
        notUnitTypeValue = 0
        assert feetValue == notUnitTypeValue


def test_givenTwoDifferentValuesOfFeetType_WhenCompared_ShouldReturnFalse():
    feetValue1 = QuantityMeasurement(Unit.Feet, 2)
    feetValue2 = QuantityMeasurement(Unit.Feet, 7)
    assert (feetValue1 == feetValue2) == False


# Test cases for Inch


def test_givenZeroInchAndZeroInch_WhenCompared_ShouldReturnTrue():
    inchValue1 = QuantityMeasurement(Unit.Inch, 0)
    inchValue2 = QuantityMeasurement(Unit.Inch, 0)
    assert inchValue1 == inchValue2


def test_givenTwoSameInchValues_WhenComparedIfTypeMissMatched_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        inchValue1 = QuantityMeasurement(Unit.Inch, 0)
        inchValue2 = float(0.0)
        assert inchValue1 == inchValue2


def test_givenTwoDifferentValuesOfInchType_WhenCompared_ShouldReturnFalse():
    inchValue1 = QuantityMeasurement(Unit.Inch, 4)
    inchValue2 = QuantityMeasurement(Unit.Inch, 7)
    assert (inchValue1 == inchValue2) == False


# Test Cases for 1 Feet = 12 Inch


def test_given_1FeetAnd_12Inch_WhenCompared_ShouldReturnTrue():
    feetValue = QuantityMeasurement(Unit.Feet, 1)
    inchValue = QuantityMeasurement(Unit.Inch, 12)
    assert feetValue == inchValue


def test_given_12InchAnd_1Feet_WhenCompared_ShouldReturnTrue():
    inchValue = QuantityMeasurement(Unit.Inch, 12)
    feetValue = QuantityMeasurement(Unit.Feet, 1)
    assert inchValue == feetValue


def test_given_5FeetAnd_60Inch_WhenComapared_ShouldReturnTrue():
    feetValue = QuantityMeasurement(Unit.Feet, 5)
    inchValue = QuantityMeasurement(Unit.Inch, 60)
    assert feetValue == inchValue


def test_given_60InchAnd_5Feet_WhenComapared_ShouldReturnTrue():
    inchValue = QuantityMeasurement(Unit.Inch, 60)
    feetValue = QuantityMeasurement(Unit.Feet, 5)
    assert inchValue == feetValue


def test_given_5Inch_60Feet_WhenCompared_ShouldReturnFalse():
    inchValue = QuantityMeasurement(Unit.Inch, 5)
    feetValue = QuantityMeasurement(Unit.Feet, 60)
    assert (inchValue == feetValue) == False


# Test cases for Yard

def test_givenZeroYardAndZeroYard_WhenCompared_ShouldReturnTrue():
    yardValue1 = QuantityMeasurement(Unit.Yard, 0)
    yardValue2 = QuantityMeasurement(Unit.Yard, 0)
    assert yardValue1 == yardValue2


def test_givenTwoSameYardValues_WhenComparedIfTypeMissMatched_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        yardValue1 = QuantityMeasurement(Unit.Yard, 0)
        yardValue2 = float(0.0)
        assert yardValue1 == yardValue2


def test_givenTwoDifferentValuesOfYardType_WhenCompared_ShouldReturnFalse():
    yardValue1 = QuantityMeasurement(Unit.Yard, 14)
    yardValue2 = QuantityMeasurement(Unit.Yard, 4)
    assert (yardValue1 == yardValue2) == False


def test_given_3FeetAnd_1Yard_WhenCompared_ShouldReturnTrue():
    assert QuantityMeasurement(Unit.Feet, 3.0) == QuantityMeasurement(Unit.Yard, 1.0)


def test_given_1FeetAnd_1Yard_WhenCompared_ShouldReturnFalse():
    assert (QuantityMeasurement(Unit.Feet, 1.0) == QuantityMeasurement(Unit.Yard, 1.0)) == False


def test_given_1YardAnd_36Inch_WhenCompared_ShouldReturnTrue():
    assert QuantityMeasurement(Unit.Yard, 1.0) == QuantityMeasurement(Unit.Inch, 36.0)


def test_given_36InchAnd_1Yard_WhenCompared_ShouldReturnTrue():
    assert QuantityMeasurement(Unit.Inch, 36.0) == QuantityMeasurement(Unit.Yard, 1.0)


def test_given_1YardAnd_3Feet_WhenCompared_ShouldReturnTrue():
    assert QuantityMeasurement(Unit.Yard, 1.0) == QuantityMeasurement(Unit.Feet, 3.0)


def test_given_1InchAnd_1Yard_WhenCompared_ShouldReturnFalse():
    assert (QuantityMeasurement(Unit.Inch, 1.0) == QuantityMeasurement(Unit.Yard, 1.0)) == False


# Test cases for Centimetre

def test_givenZeroCentimetreAndZeroCentimetre_WhenCompared_ShouldReturnTrue():
    assert QuantityMeasurement(Unit.Centimetre, 0.0) == QuantityMeasurement(Unit.Centimetre, 0)


def test_givenTwoSameCentimetreValues_WhenComparedIfTypeMissMatched_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        assert QuantityMeasurement(Unit.Centimetre, 1) == float(1.0)


def test_givenTwoDifferentValuesOfCentimetreType_WhenCompared_ShouldReturnFalse():
    assert (QuantityMeasurement(Unit.Centimetre, 2) == QuantityMeasurement(Unit.Centimetre, 1)) == False


def test_given_2InchAnd_5Centimetre_WhenCompared_ShouldReturnTrue():
    assert QuantityMeasurement(Unit.Inch, 2) == QuantityMeasurement(Unit.Centimetre, 5)


def test_given_5CentimetreAnd_2Inch_WhenCompared_ShouldReturnTrue():
    assert QuantityMeasurement(Unit.Centimetre, 5) == QuantityMeasurement(Unit.Inch, 2)


@pytest.mark.parametrize("Unit1,Unit2,expected",
                         [
                             (QuantityMeasurement(Unit.Inch, 2), QuantityMeasurement(Unit.Feet, 5), False),
                             (QuantityMeasurement(Unit.Inch, 2), QuantityMeasurement(Unit.Yard, 5), False),
                             (QuantityMeasurement(Unit.Centimetre, 5), QuantityMeasurement(Unit.Yard, 2), False),
                             (QuantityMeasurement(Unit.Centimetre, 5), QuantityMeasurement(Unit.Yard, 2), False),

                         ])
def test_given_2InchWithOtherUnitType_WhenCompared_ShouldReturnFalse(Unit1, Unit2, expected):
    assert (Unit1 == Unit2) == expected


# Test cases for Unit additions

@pytest.mark.parametrize("Unit1,Unit2,expected",
                         [
                             (QuantityMeasurement(Unit.Feet, 0), QuantityMeasurement(Unit.Feet, 0),
                              QuantityMeasurement(Unit.Feet, 0)),
                             (QuantityMeasurement(Unit.Inch, 0), QuantityMeasurement(Unit.Inch, 0),
                              QuantityMeasurement(Unit.Inch, 0)),
                             (QuantityMeasurement(Unit.Yard, 0), QuantityMeasurement(Unit.Yard, 0),
                              QuantityMeasurement(Unit.Yard, 0)),
                             (QuantityMeasurement(Unit.Centimetre, 0), QuantityMeasurement(Unit.Centimetre, 0),
                              QuantityMeasurement(Unit.Centimetre, 0))
                         ])
def test_givenZeroUnitOfSameType_WhenAdded_ShouldReturnZeroUnitOfSameType(Unit1, Unit2, expected):
    assert (Unit1 + Unit2) == expected


def test_given_2inchAnd_2Inch_WhenAdded_ShouldReturn_4Inch():
    assert QuantityMeasurement(Unit.Inch, 2) + QuantityMeasurement(Unit.Inch, 2) == QuantityMeasurement(Unit.Inch,
                                                                                                            4)


def test_given_1FeetAnd_2Inch_WhenAdded_ShouldReturn_14Inch():
    assert QuantityMeasurement(Unit.Feet, 1) + QuantityMeasurement(Unit.Inch, 2) == QuantityMeasurement(Unit.Inch,
                                                                                                            14)


def test_given_1FeetAnd_1Feet_WhenAdded_ShouldReturn_24Inch():
    assert QuantityMeasurement(Unit.Feet, 1) + QuantityMeasurement(Unit.Feet, 1) == QuantityMeasurement(Unit.Inch,
                                                                                                            24)


def test_given_2InchAnd_2Point5Centimetre_WhenAdded_ShouldReturn_3Inch():
    assert QuantityMeasurement(Unit.Inch, 2) + QuantityMeasurement(Unit.Centimetre, 2.5) == QuantityMeasurement(
        Unit.Inch, 3)


@pytest.mark.parametrize("Unit1,Unit2,expected",
                         [
                             (QuantityMeasurement(Unit.Inch, 0), QuantityMeasurement(Unit.Feet, 0),
                              QuantityMeasurement(Unit.Centimetre, 0)),
                             (QuantityMeasurement(Unit.Inch, 0), QuantityMeasurement(Unit.Yard, 0),
                              QuantityMeasurement(Unit.Inch, 0)),
                             (QuantityMeasurement(Unit.Centimetre, 0), QuantityMeasurement(Unit.Yard, 0),
                              QuantityMeasurement(Unit.Yard, 0)),
                             (QuantityMeasurement(Unit.Centimetre, 0), QuantityMeasurement(Unit.Yard, 0),
                              QuantityMeasurement(Unit.Feet, 0)),
                             (QuantityMeasurement(Unit.Inch, 0), QuantityMeasurement(Unit.Feet, 0),
                              QuantityMeasurement(Unit.Feet, 0)),
                             (QuantityMeasurement(Unit.Inch, 0), QuantityMeasurement(Unit.Yard, 0),
                              QuantityMeasurement(Unit.Centimetre, 0)),
                             (QuantityMeasurement(Unit.Centimetre, 0), QuantityMeasurement(Unit.Yard, 0),
                              QuantityMeasurement(Unit.Inch, 0)),
                             (QuantityMeasurement(Unit.Centimetre, 0), QuantityMeasurement(Unit.Yard, 0),
                              QuantityMeasurement(Unit.Feet, 0)),
                         ])
def test_givenValuesAszeroForAnyTypes_WhenAdded_ShouldReturnValueAsZeroForAnyType(Unit1, Unit2, expected):
    assert Unit1 + Unit2 == expected


# test cases for UC 5
@pytest.mark.parametrize("vol1,vol2,expected",
                         [
                             (QuantityMeasurement(Unit.Gallon, 0), QuantityMeasurement(Unit.Gallon, 0), True),
                             (QuantityMeasurement(Unit.Liter, 0), QuantityMeasurement(Unit.Liter, 0), True),
                             (QuantityMeasurement(Unit.Ml, 0), QuantityMeasurement(Unit.Ml, 0), True),
                             (QuantityMeasurement(Unit.Gallon, 0), QuantityMeasurement(Unit.Liter, 0), True),
                             (QuantityMeasurement(Unit.Gallon, 0), QuantityMeasurement(Unit.Ml, 0), True),
                             (QuantityMeasurement(Unit.Ml, 0), QuantityMeasurement(Unit.Liter, 0), True),
                         ])
def test_givenZeroUnitOfAnyVolumeAndZeroUnitOfAnyVolume_WhenCompared_ShouldReturnTrue(vol1, vol2, expected):
    assert (vol1 == vol2) == expected


@pytest.mark.parametrize("vol1,vol2,expected",
                         [
                             (QuantityMeasurement(Unit.Gallon, 1), QuantityMeasurement(Unit.Liter, 3.78), True),
                             (QuantityMeasurement(Unit.Liter, 1), QuantityMeasurement(Unit.Ml, 1000), True),
                             (QuantityMeasurement(Unit.Gallon, 1), QuantityMeasurement(Unit.Ml, 3780), True),
                             (QuantityMeasurement(Unit.Gallon, 1), QuantityMeasurement(Unit.Liter, 378), False),
                             (QuantityMeasurement(Unit.Liter, 1), QuantityMeasurement(Unit.Ml, 100), False),
                         ])
def test_givenTwoDifferentVolumes_WhenCompared_ShouldMeetExpectations(vol1, vol2, expected):
    assert (vol1 == vol2) == expected


@pytest.mark.parametrize("vol1,vol2,expectedVol",
                         [
                             (QuantityMeasurement(Unit.Gallon, 1), QuantityMeasurement(Unit.Liter, 3.78),
                              QuantityMeasurement(Unit.Liter, 7.56)),
                             (QuantityMeasurement(Unit.Liter, 1), QuantityMeasurement(Unit.Ml, 1000),
                              QuantityMeasurement(Unit.Liter, 2)),
                             (QuantityMeasurement(Unit.Gallon, 1), QuantityMeasurement(Unit.Ml, 3780),
                              QuantityMeasurement(Unit.Ml, 7560)),
                         ])
def test_givenTwoDifferentVolumes_WhenAdded_ShouldReturnExpectedValue(vol1, vol2, expectedVol):
    assert vol1 + vol2 == expectedVol
