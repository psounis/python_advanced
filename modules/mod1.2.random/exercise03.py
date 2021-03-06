from random import paretovariate
from math import floor,inf

stats={}

for i in range(0,3):
    stats[(i,i+1)]=0
stats[(3,inf)]=0


for i in range(1000000):
    v=paretovariate(3)
    s=floor(v)
    f=s+1
    if s<=2:
        stats[(s,f)]+=1
    else:
        stats[(3,inf)]+=1

for i in range(0,3):
    print(f"stats[({i},{i+1})]={stats[(i,i+1)]/10000:.2f}%")
print(f"stats[(3,inf)]={stats[(3,inf)]/10000:.2f}%")