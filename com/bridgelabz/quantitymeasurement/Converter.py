from com.bridgelabz.quantitymeasurement.Unit import Length, Volume, Weight, Temperature


class Converter:
    BaseUnitDict = {
        type(Length.Inch): Length.Inch,
        type(Volume.Ml): Volume.Ml,
        type(Weight.Gram): Weight.Gram,
        type(Temperature.C): Temperature.C
    }

    @staticmethod
    def convert(value1Unit, value2Unit, value1, value2):
        if isinstance(value1Unit, Temperature):
            value1 = value1Unit.value * (value1 if value1Unit is Temperature.C else value1 - 32)
            value2 = value2Unit.value * (value2 if value2Unit is Temperature.C else value2 - 32)
            return value1, value2
        value1 = value1Unit.value * value1
        value2 = value2Unit.value * value2
        return value1, value2
