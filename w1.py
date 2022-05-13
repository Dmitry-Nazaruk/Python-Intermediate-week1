class FractionMixin:

    @staticmethod
    def add(fr1, fr2):
        result = (fr1.num / fr1.den) + (fr2.num / fr2.den)
        return result

    @staticmethod
    def sub(fr1, fr2):
        result = (fr1.num / fr1.den) - (fr2.num / fr2.den)
        return result

    @staticmethod
    def mul(fr1, fr2):
        result = (fr1.num / fr1.den) * (fr2.num / fr2.den)
        return result

    @staticmethod
    def div(fr1, fr2):
        result = (fr1.num / fr1.den) / (fr2.num / fr2.den)
        return result


class Fraction(FractionMixin):

    def __init__(self, num: int, den: int):
        self.__num = num
        self.__den = den

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    def __add__(self, other):
        result = (self.num / self.den) + (other.num / other.den)
        return result

    def __sub__(self, other):
        result = (self.num / self.den) - (other.num / other.den)
        return result

    def __mul__(self, other):
        result = (self.num / self.den) * (other.num / other.den)
        return result

    def __truediv__(self, other):
        result = (self.num / self.den) / (other.num / other.den)
        return result

    @classmethod
    def from_string(cls, str_value):
        values = [int(i) for i in str_value.split(',')]
        assert len(values) == 2
        return cls(*values)

    def __str__(self):
        return f'{self.num} / {self.den}'


fr1 = Fraction(10, 20)
fr2 = Fraction.from_string('20,10')
print(fr1.div(fr1, fr2))
print(fr1.add(fr1, fr2))
print(fr1.mul(fr1, fr2))
print(fr1.sub(fr1, fr2))
print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)
print(fr1.num, fr2.den)
print(fr1)
