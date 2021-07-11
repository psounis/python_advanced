import json
from random import randrange

with open("ob.json", "w") as f:
    json.dump([(1,2),(2,3)], f)
with open("ob.json", "r") as f:
    ob = json.load(f)
    print(ob)

with open("multi_line.json", "w") as f:
    for _ in range(4):
        v = randrange(3)
        if v == 0:
            json.dump([1,2,3], f)
        elif v == 1:
            json.dump({"a":1, "b":2, "c":3}, f)
        else:
            json.dump(4, f)
        f.write("\n")

with open("multi_line.json", "r") as f:
    for lineObj in f:
        print(json.loads(lineObj))