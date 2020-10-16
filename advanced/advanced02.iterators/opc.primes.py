# modification on
# https://school.geekwall.in/p/r1halvojG/what-can-you-use-python-generator-functions-for

def check_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

class Primes:
    def __init__(self):
        self.number = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.number += 1
        if check_prime(self.number):
            return self.number
        else:
            return self.__next__()

primes = Primes()
print(primes)
for x in primes:
    print(x)