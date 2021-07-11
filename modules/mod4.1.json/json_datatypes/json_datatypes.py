import json

with open("ob.json", "w") as f:
    json.dump(1, f)
    f.write("\n")
    json.dump(1.1, f)
    f.write("\n")
    json.dump("string", f)
    f.write("\n")
    json.dump([1, 2], f)
    f.write("\n")
    json.dump((1, 2), f)
    f.write("\n")
    # json.dump({1, 2}, f)
    json.dump({1: 1, 2: 2}, f)
    f.write("\n")

with open("ob.json", "r") as f:
    for line in f:
        print(type(json.loads(line)))
