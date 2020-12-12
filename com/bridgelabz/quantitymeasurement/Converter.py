from com.bridgelabz.quantitymeasurement.Unit import Length, Volume, Weight


class Converter:
    BaseUnitDict = {
        type(Length.Inch): Length.Inch,
        type(Volume.Ml): Volume.Ml,
        type(Weight.Gram): Weight.Gram
    }
    @staticmethod
    def convert(value1Unit, value2Unit, value1, value2):
        value1 = value1Unit.value * value1
        value2 = value2Unit.value * value2
        return value1, value2
