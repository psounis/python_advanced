from decimal import Decimal

D = Decimal

print(D(1))
print(D('3.14'))
print(D(3.14))
print(D('3.1400000000000001243449787580175325274467468261718751123123'))
print(D((1,(1,4,1,5),-1)))
print(D("NaN"))
print(D("infinity"))
print(D("-infinity"))

