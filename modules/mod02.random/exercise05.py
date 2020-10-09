from random import getrandbits

x = getrandbits(8)

print(f"x={x}=",end="")
bits=[]
for i in range(8):
    bits = [x%2] + bits
    x = x//2

for i in range(8):
    print(bits[i], end="")
