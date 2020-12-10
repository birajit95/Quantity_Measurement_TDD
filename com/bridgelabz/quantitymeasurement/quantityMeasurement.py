from com.bridgelabz.quantitymeasurement.InvalidTypeException import InvalidTypeException
from com.bridgelabz.quantitymeasurement.InvalidTypeException import ExceptionType


class Length:
    def __init__(self, length):
        if type(length) is not float and type(length) is not int:
            raise InvalidTypeException(ExceptionType.NOT_A_NUMBER_TYPE_EXCEPTION.value)
        self.length = length

    def __eq__(self, other):
        if type(self) == type(other):
            return self.length == other.length
        elif isinstance(self, Feet) and isinstance(other, Inch):
            return other.length == self.length * 12
        elif isinstance(self, Inch) and isinstance(other, Feet):
            return other.length * 12 == self.length
        elif isinstance(self, Feet) and isinstance(other, Yard):
            return other.length * 3 == self.length
        elif isinstance(self, Yard) and isinstance(other, Feet):
            return other.length == self.length * 3
        elif isinstance(self, Inch) and isinstance(other, Yard):
            return other.length * 36 == self.length
        elif isinstance(self, Yard) and isinstance(other, Inch):
            return other.length == self.length * 36
        elif isinstance(self, Inch) and isinstance(other, Centimetre):
            return other.length == self.length * 2.5
        elif isinstance(self, Centimetre) and isinstance(other, Inch):
            return other.length * 2.5 == self.length
        elif type(self) != type(other) and self.length == other:
            raise InvalidTypeException(ExceptionType.NOT_LENGTH_TYPE_EXCEPTION.value)

    @staticmethod
    def convertLength(length1, length2):
        if isinstance(length1, Feet) and isinstance(length2, Inch):
            return length1.length * 12


class Feet(Length):
    def __init__(self, feet):
        super().__init__(length=feet)

    def __eq__(self, other):
        return super().__eq__(other)

    def __add__(self, other):
        if isinstance(other, Inch):
            convertedLength = Length.convertLength(self, other)
            other.length = other.length + convertedLength
            return other
        self.length = self.length + other.length
        return self


class Inch(Length):
    def __init__(self, inch):
        super().__init__(length=inch)

    def __eq__(self, other):
        return super().__eq__(other)

    def __add__(self, other):
        self.length = self.length + other.length
        return self


class Yard(Length):
    def __init__(self, yard):
        super().__init__(length=yard)

    def __eq__(self, other):
        return super().__eq__(other)

    def __add__(self, other):
        self.length = self.length + other.length
        return self


class Centimetre(Length):
    def __init__(self, cm):
        super().__init__(length=cm)

    def __eq__(self, other):
        return super().__eq__(other)

    def __add__(self, other):
        self.length = self.length + other.length
        return self


if __name__ == '__main__':
    print("Welcome to Quantity Measurement Problem")