from random import triangular
from math import floor

stats={}

for i in range(0,10):
    stats[(i/10,(i+1)/10)]=0

for i in range(1000000):
    v=triangular(0, 1)
    s=floor(v*10)/10
    f=floor((v+0.1)*10)/10
    stats[(s,f)]+=1

for i in range(0,10):
    print(f"stats[({i/10},{(i+1)/10})]={stats[(i/10,(i+1)/10)]/10000:.2f}%")
