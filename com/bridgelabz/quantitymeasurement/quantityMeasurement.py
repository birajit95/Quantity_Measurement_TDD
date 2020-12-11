from com.bridgelabz.quantitymeasurement.InvalidTypeException import InvalidTypeException
from com.bridgelabz.quantitymeasurement.InvalidTypeException import ExceptionType
from com.bridgelabz.quantitymeasurement.Unit import Length, Volume
from com.bridgelabz.quantitymeasurement.Converter import Converter


class QuantityMeasurement:
    def __init__(self, unit, value):
        if type(value) is not float and type(value) is not int:
            raise InvalidTypeException(ExceptionType.NOT_A_NUMBER_TYPE_EXCEPTION.value)
        self.__value = value
        self.__unit = unit

    def __eq__(self, other):
        if isinstance(other, QuantityMeasurement) and type(self.__unit) == type(other.__unit):
            if self.__unit != other.__unit and self.__value == other.__value == 0:
                value1, value2 = Converter.convert(self.__unit, other.__unit, self.__value, other.__value)
                return value1 == value2
            if self.__unit == other.__unit and self.__value == other.__value:
                return True
            elif self.__unit == other.__unit and self.__value != other.__value:
                return False
            elif self.__unit != other.__unit and self.__value == other.__value:
                return False
            else:
                value1, value2 = Converter.convert(self.__unit, other.__unit, self.__value, other.__value)
                return value1 == value2
        raise InvalidTypeException(ExceptionType.COMPARISON_NOT_POSSIBLE_EXCEPTION.value)

    def __add__(self, other):
        if isinstance(other, QuantityMeasurement) and type(self.__unit) == type(other.__unit):
            if self.__value == other.__value == 0:
                return self
            value1, value2 = Converter.convert(self.__unit, other.__unit, self.__value, other.__value)
            other.__value = value1 + value2
            other.__unit = Length.Inch if isinstance(other.__unit, Length) else Volume.Ml  # applying the base rule
            return other
        raise InvalidTypeException(ExceptionType.ADDITION_NOT_POSSIBLE_EXCEPTION.value)


if __name__ == '__main__':
    print("Welcome to Quantity Measurement Problem")
