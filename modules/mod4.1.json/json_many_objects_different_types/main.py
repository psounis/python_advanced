from timeclass import Time, ZonedTime, time_encoder, time_decoder
from random import randrange
import json

arr = []
for i in range(10):
    if randrange(2)==0:
        t = Time(randrange(24), randrange(60), randrange(60))
    else:
        t = ZonedTime(randrange(24), randrange(60), randrange(60), "UTC+" + str(randrange(10)))
    arr.append(t)

with open("ob.json", "w") as f:
    json.dump(arr, f, default=time_encoder)

with open("ob.json", "r") as f:
    data = json.load(f, object_hook=time_decoder)
    for t in data:
        print(t)