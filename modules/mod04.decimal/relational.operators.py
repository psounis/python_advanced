# relational.operators.py
from decimal import Decimal
D=Decimal

print(D("12.0") == D("12"))
print(D("3.0") != D("3.000"))
print(D("1.1") < D("1.11"))
print(D("1.1") <= D("1.11"))
print(D("1.1") > D("1.11"))
print(D("1.1") >= D("1.11"))