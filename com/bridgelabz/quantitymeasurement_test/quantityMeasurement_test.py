from com.bridgelabz.quantitymeasurement.quantityMeasurement import Feet
from com.bridgelabz.quantitymeasurement.quantityMeasurement import Inch
from com.bridgelabz.quantitymeasurement.quantityMeasurement import Yard
from com.bridgelabz.quantitymeasurement.quantityMeasurement import Centimetre
from com.bridgelabz.quantitymeasurement.InvalidTypeException import InvalidTypeException
import pytest


def test_givenZeroFeetAndZeroFeet_WhenCompared_ShouldReturnTrue():
    feetValue1 = Feet(0.0)
    feetValue2 = Feet(0.0)
    assert feetValue1 == feetValue2


def test_givenAFeetValue_IfNotNumberType_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        feetValue = Feet("hello")


def test_givenTwoSameValues_WhenComparedIfTypeMissMatched_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        feetValue1 = Feet(0.0)
        feetValue2 = float(0.0)
        assert feetValue1 == feetValue2


def test_givenTwoDifferentValuesOfFeetType_WhenCompared_ShouldReturnFalse():
    feetValue1 = Feet(2.0)
    feetValue2 = Feet(1.0)
    assert (feetValue1 == feetValue2) == False


# Test cases for Inch


def test_givenZeroInchAndZeroInch_WhenCompared_ShouldReturnTrue():
    inchValue1 = Inch(0.0)
    inchValue2 = Inch(0.0)
    assert inchValue1 == inchValue2


def test_givenAnInchValue_IfNotNumberType_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        inchValue = Inch("h")


def test_givenTwoSameInchValues_WhenComparedIfTypeMissMatched_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        inchValue1 = Inch(0.0)
        inchValue2 = float(0.0)
        assert inchValue1 == inchValue2


def test_givenTwoDifferentValuesOfInchType_WhenCompared_ShouldReturnFalse():
    inchValue1 = Inch(2.0)
    inchValue2 = Inch(1.0)
    assert (inchValue1 == inchValue2) == False


# Test Cases for 1 Feet = 12 Inch


def test_given_1FeetAnd_12Inch_WhenCompared_ShouldReturnTrue():
    feetValue = Feet(1.0)
    inchValue = Inch(12.0)
    assert feetValue == inchValue


def test_given_12InchAnd_1Feet_WhenCompared_ShouldReturnTrue():
    inchValue = Inch(12.0)
    feetValue = Feet(1.0)
    assert inchValue == feetValue


def test_given_5FeetAnd_60Inch_WhenComapared_ShouldReturnTrue():
    feetValue = Feet(5.0)
    inchValue = Inch(60.0)
    assert feetValue == inchValue


def test_given_60InchAnd_5Feet_WhenComapared_ShouldReturnTrue():
    inchValue = Inch(60.0)
    feetValue = Feet(5.0)
    assert inchValue == feetValue


def test_given_5Inch_60Feet_WhenCompared_ShouldReturnFalse():
    inchValue = Inch(5.0)
    feetValue = Feet(60.0)
    assert (inchValue == feetValue) == False


# Test cases for Yard

def test_givenZeroYardAndZeroYard_WhenCompared_ShouldReturnTrue():
    yardValue1 = Yard(0.0)
    yardValue2 = Yard(0.0)
    assert yardValue1 == yardValue2


def test_givenAYardValue_IfNotNumberType_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        yardValue = Yard("world")


def test_givenTwoSameYardValues_WhenComparedIfTypeMissMatched_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        yardValue1 = Yard(0.0)
        yardValue2 = float(0.0)
        assert yardValue1 == yardValue2


def test_givenTwoDifferentValuesOfYardType_WhenCompared_ShouldReturnFalse():
    yardValue1 = Feet(2.0)
    yardValue2 = Feet(1.0)
    assert (yardValue1 == yardValue2) == False


def test_given_3FeetAnd_1Yard_WhenCompared_ShouldReturnTrue():
    assert Feet(3.0) == Yard(1.0)


def test_given_1FeetAnd_1Yard_WhenCompared_ShouldReturnFalse():
    assert (Feet(1.0) == Yard(1.0)) == False


def test_given_1YardAnd_36Inch_WhenCompared_ShouldReturnTrue():
    assert Yard(1.0) == Inch(36.0)


def test_given_36InchAnd_1Yard_WhenCompared_ShouldReturnTrue():
    assert Inch(36.0) == Yard(1.0)


def test_given_1YardAnd_3Feet_WhenCompared_ShouldReturnTrue():
    assert Yard(1.0) == Feet(3.0)


def test_given_1InchAnd_1Yard_WhenCompared_ShouldReturnFalse():
    assert (Inch(1.0) == Yard(1.0)) == False


# Test cases for Centimetre

def test_givenZeroCentimetreAndZeroCentimetre_WhenCompared_ShouldReturnTrue():
    assert Centimetre(0.0) == Centimetre(0)


def test_givenACentimetreValue_IfNotNumberType_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        feetValue = Centimetre("hello")


def test_givenTwoSameCentimetreValues_WhenComparedIfTypeMissMatched_ShouldRaise_InvalidTypeException():
    with pytest.raises(InvalidTypeException):
        assert Centimetre(1) == float(1.0)


def test_givenTwoDifferentValuesOfCentimetreType_WhenCompared_ShouldReturnFalse():
    assert (Centimetre(2) == Centimetre(1)) == False


def test_given_2InchAnd_5Centimetre_WhenCompared_ShouldReturnTrue():
    assert Inch(2) == Centimetre(5)


def test_given_5CentimetreAnd_2Inch_WhenCompared_ShouldReturnTrue():
    assert Centimetre(5) == Inch(2)


@pytest.mark.parametrize("length1,length2,expected",
                         [
                             (Inch(2), Feet(5), False),
                             (Inch(2), Yard(5), False),

                         ])
def test_given_2InchWithOtherLengthType_WhenCompared_ShouldReturnFalse(length1, length2, expected):
    assert (length1 == length2) == expected

# Test cases for Length additions

@pytest.mark.parametrize("length1,length2,expected",
                         [
                             (Feet(0), Feet(0), Feet(0)),
                             (Inch(0), Inch(0), Inch(0)),
                             (Yard(0), Yard(0), Yard(0)),
                             (Centimetre(0), Centimetre(0), Centimetre(0))
                         ])
def test_givenZeroUnitOfSameType_WhenAdded_ShouldReturnZeroUnitOfSameType(length1,length2,expected):
    assert (length1 + length2) == expected
