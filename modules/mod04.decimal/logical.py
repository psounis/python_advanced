from decimal import Decimal, getcontext
D=Decimal

x=D(1)
y=D(110)

print(x.logical_and(y))
print(x.logical_or(y))
print(x.logical_xor(y))
getcontext().prec=8
print(x.logical_invert())