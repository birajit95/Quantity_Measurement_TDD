from com.bridgelabz.quantitymeasurement.InvalidTypeException import InvalidTypeException
from com.bridgelabz.quantitymeasurement.InvalidTypeException import ExceptionType

class Feet:
    def __init__(self, feet):
        if type(feet) is not float:
            raise InvalidTypeException(ExceptionType.NOT_FLOAT_TYPE_EXCEPTION.value)
        self.feet = feet

    def __eq__(self, other):
        return self.feet == other.feet


if __name__ == '__main__':
    print("Welcome to Quantity Measurement Problem")