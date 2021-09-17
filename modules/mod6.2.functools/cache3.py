from functools import cached_property


class Calcs:
    def __init__(self):
        self._val = 0

    @cached_property
    def val(self):
        print("some tedious calc...")
        self._val = 100
        return self._val


calcs = Calcs()
print(calcs.val)
print(calcs.val)

