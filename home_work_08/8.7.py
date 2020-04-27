class ComplexNumber:
    def __init__(self, d, m):
        self.d = d
        self.m = m

    @staticmethod
    def sing_def(param):
        sing = '+' if param > 0 else '-'
        return sing

    def __str__(self):
        return f"z = {self.d} {ComplexNumber.sing_def(self.m)} {abs(self.m)} * i"

    def __add__(self, other):
        return f"z = {self.d + other.d} {ComplexNumber.sing_def(self.m + other.m)} {abs(self.m + other.m)} * i"

    def __mul__(self, other):
        mul_d = self.d * other.d + (-(self.m * other.m))
        mul_m = self.d * other.m + self.m * other.d
        return f"z = {mul_d} {ComplexNumber.sing_def(mul_m)} {abs(mul_m)} * i"


my_1 = ComplexNumber(-6, -3)
my_2 = ComplexNumber(2, 5)
print(my_1)
print(my_2)
print(my_1 + my_2)
print(my_1 * my_2)
