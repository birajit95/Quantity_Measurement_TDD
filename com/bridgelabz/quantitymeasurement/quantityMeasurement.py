from com.bridgelabz.quantitymeasurement.InvalidTypeException import InvalidTypeException
from com.bridgelabz.quantitymeasurement.InvalidTypeException import ExceptionType
import enum


class QuantityMeasurement:
    def __init__(self, unit, value):
        if type(value) is not float and type(value) is not int:
            raise InvalidTypeException(ExceptionType.NOT_A_NUMBER_TYPE_EXCEPTION.value)
        self.__value = value
        self.__unit = unit

    def __eq__(self, other):
        if isinstance(other, QuantityMeasurement):
            if self.__unit == other.__unit and self.__value == other.__value:
                return True
            elif self.__unit == other.__unit and self.__value != other.__value:
                return False
            elif self.__unit != other.__unit and self.__value == other.__value:
                return False
            else:
                value1, value2 = convert(self.__unit, other.__unit, self.__value, other.__value)
                return value1 == value2
        raise InvalidTypeException(ExceptionType.NOT_LENGTH_TYPE_EXCEPTION.value)


class Length(enum.Enum):
    Inch = 1.0
    Feet = 12.0
    Yard = 36.0
    Centimetre = 0.4


def convert(value1Unit, value2Unit, value1, value2):
    value1 = value1Unit.value * value1
    value2 = value2Unit.value * value2
    return value1, value2


if __name__ == '__main__':
    print("Welcome to Quantity Measurement Problem")