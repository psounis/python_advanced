class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:" \
               f"{str(self.minute).zfill(2)}:" \
               f"{str(self.second).zfill(2)}"


class ZonedTime(Time):
    def __init__(self, hour, minute, second, zone):
        super().__init__(hour, minute, second)
        self.zone = zone

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:" \
               f"{str(self.minute).zfill(2)}:" \
               f"{str(self.second).zfill(2)} " + self.zone


def time_encoder(time):
    if isinstance(time, ZonedTime):
        return {"__ZonedTime__": True, "hour": time.hour, "minute": time.minute,
                "second": time.second, "zone": time.zone}
    elif isinstance(time, Time):
        return {"__Time__": True, "hour": time.hour, "minute": time.minute,
                "second": time.second}
    else:
        raise TypeError("Type should be Time")


def time_decoder(time):
    if "__Time__" in time:
        return Time(time["hour"], time["minute"], time["second"])
    elif "__ZonedTime__" in time:
        return ZonedTime(time["hour"], time["minute"], time["second"], time["zone"])
