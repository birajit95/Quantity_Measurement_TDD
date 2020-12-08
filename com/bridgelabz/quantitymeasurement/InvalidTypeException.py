import enum


class ExceptionType(enum.Enum):
    NOT_FLOAT_TYPE_EXCEPTION = "Given value is not a float type. It must be a float type"


class InvalidTypeException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return f"{self.message}"
