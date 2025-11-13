from abc import ABC, abstractmethod

class RationalNumber:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

class Equality(ABC):
    @abstractmethod
    def is_equal(self, other):
        pass

class Comparison(RationalNumber, Equality):
    def __init__(self, numerator, denominator):
        super().__init__(numerator, denominator)
    def is_equal(self, other):
        if not isinstance(other, RationalNumber):
            return False
        return self.numerator * other.denominator == other.numerator * self.denominator

if __name__ == "__main__":
    a1 = Comparison(1, 2)
    a2 = Comparison(8, 16)
    a3 = Comparison(2, 9)
    print(f"Сравнение {a1} и {a2}: {a1.is_equal(a2)}")
    print(f"Сравнение {a1} и {a3}: {a1.is_equal(a3)}")