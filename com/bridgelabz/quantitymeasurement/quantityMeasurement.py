from com.bridgelabz.quantitymeasurement.InvalidTypeException import InvalidTypeException
from com.bridgelabz.quantitymeasurement.InvalidTypeException import ExceptionType

class Feet:
    def __init__(self, feet):
        if type(feet) is not float:
            raise InvalidTypeException(ExceptionType.NOT_FLOAT_TYPE_EXCEPTION.value)
        self.feet = feet

    def __eq__(self, other):
        if not isinstance(other, Feet) and self.feet == other:
            raise InvalidTypeException(ExceptionType.NOT_FEET_TYPE_EXCEPTION.value)
        return self.feet == other.feet


if __name__ == '__main__':
    print("Welcome to Quantity Measurement Problem")