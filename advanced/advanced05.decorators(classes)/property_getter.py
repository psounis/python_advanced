class Salary:
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount


s = Salary(500)
print(s.amount)