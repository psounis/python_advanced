from functools import partialmethod


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:" \
               f"{str(self.minute).zfill(2)}:" \
               f"{str(self.second).zfill(2)}"

    def __gt__(self, other):
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour:
            if self.minute > other.minute:
                return True
            elif self.minute == other.minute:
                if self.second > other.second:
                    return True
        return False

    def __eq__(self, other):
        if self.hour == other.hour and self.minute == other.minute and self.second == other.second:
            return True
        return False

    def set_hour(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    set_midnight = partialmethod(set_hour, 0, 0, 0)
    set_half = partialmethod(set_hour, minute=30, second=0)


t = Time(11, 1, 2)
print(t)
t.set_midnight()
print(t)
t.set_half(22)
print(t)
