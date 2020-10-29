#quantize.py
from decimal import Decimal
D=Decimal
fpacc=Decimal(10) ** -2

a=Decimal("0.43")
b=Decimal("12.93")
print(a*b)
print((a*b).quantize(fpacc))
