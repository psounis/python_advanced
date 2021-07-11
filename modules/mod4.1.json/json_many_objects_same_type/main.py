from timeclass import Time, time_encoder, time_decoder
from random import randrange
import json

arr = []
for i in range(10):
    t = Time(randrange(24), randrange(60), randrange(60))
    arr.append(t)

with open("ob.json", "w") as f:
    json.dump(arr, f, default=time_encoder)

with open("ob.json", "r") as f:
    data = json.load(f, object_hook=time_decoder)
    for t in data:
        print(t)