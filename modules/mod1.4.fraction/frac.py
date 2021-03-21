import math
from fractions import Fraction
from decimal import Decimal

f1 = Fraction(1/3)
f2 = Fraction("1/3")
f3 = Fraction(Decimal(1.2))
f4 = Fraction(-1, 5)
print(f1, f2, f3, f4, f4.numerator, f4.denominator)

print(f3.limit_denominator(100))
print(f3.limit_denominator())
print(f3.limit_denominator().as_integer_ratio())

print((f1*f4).limit_denominator())
print(f1/f2)
print((f1+f2+f3).limit_denominator())

print(Fraction(math.sqrt(Fraction("1/9"))).limit_denominator())
print(round(Fraction("529/3"),1))
print(Fraction(math.pow(Fraction(1/3), Fraction(1/3))).limit_denominator())
