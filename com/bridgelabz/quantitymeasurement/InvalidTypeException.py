import enum


class ExceptionType(enum.Enum):
    NOT_A_NUMBER_TYPE_EXCEPTION = "Given value is not a number"
    COMPARISON_NOT_POSSIBLE_EXCEPTION = "Comparison between both types is not possible"
    ADDITION_NOT_POSSIBLE_EXCEPTION = "Addition between both is not possible"


class InvalidTypeException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return f"{self.message}"
