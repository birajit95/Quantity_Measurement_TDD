from com.bridgelabz.quantitymeasurement.InvalidTypeException import InvalidTypeException
from com.bridgelabz.quantitymeasurement.InvalidTypeException import ExceptionType


class Feet:
    def __init__(self, feet):
        if type(feet) is not float:
            raise InvalidTypeException(ExceptionType.NOT_FLOAT_TYPE_EXCEPTION.value)
        self.feet = feet

    def __eq__(self, other):
        if isinstance(other, Yard):
            return self.feet == other.yard * 3
        if isinstance(other, Inch):
            return other.inch == self.feet * 12
        if not isinstance(other, Feet) and self.feet == other:
            raise InvalidTypeException(ExceptionType.NOT_FEET_TYPE_EXCEPTION.value)
        return self.feet == other.feet


class Inch:
    def __init__(self, inch):
        if type(inch) is not float:
            raise InvalidTypeException(ExceptionType.NOT_FLOAT_TYPE_EXCEPTION.value)
        self.inch = inch

    def __eq__(self, other):
        if isinstance(other, Yard):
            return self.inch == other.yard * 36
        if isinstance(other, Feet):
            return self.inch == other.feet * 12
        if not isinstance(other, Inch) and self.inch == other:
            raise InvalidTypeException(ExceptionType.NOT_INCH_TYPE_EXCEPTION.value)
        return self.inch == other.inch


class Yard:
    def __init__(self, yard):
        if type(yard) is not float:
            raise InvalidTypeException(ExceptionType.NOT_FLOAT_TYPE_EXCEPTION.value)
        self.yard = yard

    def __eq__(self, other):
        if isinstance(other, Feet):
            return other.feet == self.yard * 3
        if isinstance(other, Inch):
            return other.inch == self.yard * 36
        if not isinstance(other, Yard) and self.yard == other:
            raise InvalidTypeException(ExceptionType.NOT_YARD_TYPE_EXCEPTION.value)
        return self.yard == other.yard


if __name__ == '__main__':
    print("Welcome to Quantity Measurement Problem")
