import enum


class ExceptionType(enum.Enum):
    NOT_A_NUMBER_TYPE_EXCEPTION = "Given value is not a number"
    NOT_LENGTH_TYPE_EXCEPTION = "Other value is not Length type"



class InvalidTypeException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return f"{self.message}"
