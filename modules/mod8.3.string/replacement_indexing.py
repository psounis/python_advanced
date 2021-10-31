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
print("minutes = {0.minute}".format(t))
l = [1, 2, 3]
print("second = {0[1]}".format(l))
d = {"a": 1, "b": 2}
print("val = {arg[a]}".format(arg=d))
