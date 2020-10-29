from decimal import Decimal, getcontext
D=Decimal

getcontext().prec = 3
a=Decimal("0.4391")
b=Decimal("12.939")
print(a,b,b/a)

print(getcontext())
