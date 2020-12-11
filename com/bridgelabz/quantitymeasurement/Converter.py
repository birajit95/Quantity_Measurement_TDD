class Converter:

    @staticmethod
    def convert(value1Unit, value2Unit, value1, value2):
        value1 = value1Unit.value * value1
        value2 = value2Unit.value * value2
        return value1, value2
