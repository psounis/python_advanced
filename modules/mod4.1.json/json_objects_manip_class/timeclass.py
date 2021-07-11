import json


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:" \
               f"{str(self.minute).zfill(2)}:" \
               f"{str(self.second).zfill(2)}"


class TimeEncoder(json.JSONEncoder):
    def default(self, time):
        if isinstance(time, Time):
            return {"hour": time.hour,
                    "minute": time.minute,
                    "second": time.second}
        else:
            raise TypeError("Type should be Time")


class TimeDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=self.decoder)

    def decoder(self, time):
        return Time(time["hour"],
                    time["minute"],
                    time["second"])
