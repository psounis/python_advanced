from math import isclose

print(isclose(0.001,0.005,abs_tol=1e-3))
print(isclose(0.0001,0.0005,abs_tol=1e-3))