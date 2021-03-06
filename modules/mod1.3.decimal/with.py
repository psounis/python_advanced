from decimal import Decimal, localcontext
D=Decimal

with localcontext() as ctx:
    ctx.prec = 500
    res = D(10) / D(3)
    print(res)