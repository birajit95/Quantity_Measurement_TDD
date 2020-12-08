class Feet:
    def __init__(self, feet):
        self.feet = feet

    def __eq__(self, other):
        return self.feet == other.feet


if __name__ == '__main__':
    print("Welcome to Quantity Measurement Problem")