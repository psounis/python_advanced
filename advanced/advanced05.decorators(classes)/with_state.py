from math import sqrt

def valid_int_gt_zero(func):
    def decorated(val):
        if not isinstance(val, int):
            raise TypeError("Not an integer")
        elif val < 0:
            raise ValueError("Negative value")
        else:
            decorated.calls += 1
            return func(val)

    decorated.calls = 0
    return decorated


@valid_int_gt_zero
def int_sqrt(val):
    return int(sqrt(val))


print(int_sqrt(2))
print(int_sqrt(4))
print("calls: " + str(int_sqrt.calls))
