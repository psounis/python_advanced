from math import comb

try:
    print(comb(11.1,6))
except ValueError:
    print("Error: Must be non-negative")
except TypeError:
    print("Error: Must be an integer")
