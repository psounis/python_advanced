from timeclass import Time, time_encoder, time_decoder
import json

t1 = Time(10, 22, 24)
print(t1)

with open("ob.json", "w") as f:
    json.dump(t1, f, default=time_encoder)

with open("ob.json", "r") as f:
    t2 = json.load(f, object_hook=time_decoder)
    print(t2)