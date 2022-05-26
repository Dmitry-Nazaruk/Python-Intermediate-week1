class FractionMixin:

    @staticmethod
    def add(fr1, fr2):
        new_den = fr1.den * fr2.den
        new_num = fr1.num * fr2.den + fr1.num * fr2.den
        return Fraction(new_num, new_den)

    @staticmethod
    def sub(fr1, fr2):
        new_den = fr1.den * fr2.den
        new_num = fr1.num * fr2.den - fr2.num * fr1.den
        return Fraction(new_num, new_den)

    @staticmethod
    def mul(fr1, fr2):
        new_den = fr1.den * fr2.den
        new_num = fr1.num * fr2.num
        return Fraction(new_num, new_den)

    @staticmethod
    def div(fr1, fr2):
        new_den = fr1.den * fr2.num
        new_num = fr1.num * fr2.den
        return Fraction(new_num, new_den)


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
        new_den = self.den * other.den
        new_num = self.num * other.den + other.num * self.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_den = self.den * other.den
        new_num = self.num * other.den - other.num * self.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_den = self.den * other.den
        new_num = self.num * other.num
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_den = self.den * other.num
        new_num = self.num * other.den
        return Fraction(new_num, new_den)

    @classmethod
    def from_string(cls, str_value):
        values = [int(i) for i in str_value.split(',')]
        assert len(values) == 2
        return cls(*values)

    def __str__(self):
        return f'{self.num} / {self.den}'


fr1 = Fraction(10, 20)
fr2 = Fraction.from_string('20,10')
print('fr1.div(fr1, fr2): ', fr1.div(fr1, fr2))
print('fr1.add(fr1, fr2): ', fr1.add(fr1, fr2))
print('fr1.mul(fr1, fr2): ', fr1.mul(fr1, fr2))
print('fr1.sub(fr1, fr2): ', fr1.sub(fr1, fr2))
print('fr1 + fr2: ', fr1 + fr2)
print('fr1 - fr2: ', fr1 - fr2)
print('fr1 * fr2: ', fr1 * fr2)
print('fr1 / fr2: ', fr1 / fr2)
print('fr1.num, fr2.den: ', fr1.num, fr2.den)
print('fr1: ', fr1)
