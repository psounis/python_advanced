class Salary:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if amount > 10000:
            raise ValueError("Too high salary")
        else:
            self._amount = amount

s = Salary(500)
print(s.amount)
s.amount = 600
print(s.amount)