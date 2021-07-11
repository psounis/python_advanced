class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:" \
               f"{str(self.minute).zfill(2)}:" \
               f"{str(self.second).zfill(2)}"


def time_encoder(time):
    if isinstance(time, Time):
        return {"hour": time.hour, "minute": time.minute, "second": time.second}
    else:
        raise TypeError("Type should be Time")


def time_decoder(time):
    return Time(time["hour"], time["minute"], time["second"])
