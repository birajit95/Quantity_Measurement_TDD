import enum


class Length(enum.Enum):
    Inch = 1.0  # base for length
    Feet = 12.0
    Yard = 36.0
    Centimetre = 0.4


class Volume(enum.Enum):
    Ml = 1.0  # base for volume
    Liter = 1000.0
    Gallon = 3780.0


class Weight(enum.Enum):
    Gram = 1.0   # base for weight
    KG = 1000.0
    Tonne = 1000000
