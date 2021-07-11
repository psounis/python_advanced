from timeclass import Time, TimeEncoder, TimeDecoder
import json

t = Time(10, 22, 24)
print(t)

with open("ob.json", "w") as f:
    json.dump(t, f, cls=TimeEncoder)

with open("ob.json", "r") as f:
    t2 = json.load(f, cls=TimeDecoder)
    print(t2)