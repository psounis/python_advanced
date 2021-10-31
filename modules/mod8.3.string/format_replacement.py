
print("{}, {}, {}".format(0, 1.1, "str"))
print("{0}, {1}, {2}".format(0, 1.1, "str"))
print("{1}, {2}, {0}".format(0, 1.1, "str"))
print("{arg1} {arg2}".format(arg1=0, arg2=1))
print("{arg2}, {arg1}, {1}, {0}".format(0, 1, arg1=0, arg2=1))


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:" \
               f"{str(self.minute).zfill(2)}:" \
               f"{str(self.second).zfill(2)}"

    def __repr__(self):
        return f"Time({self.hour},{self.minute},{self.second})"


t = Time(4, 48, 0)
print("str={0!s}\nrepr={now!r}\nascii={now}".format(t, now=t))
