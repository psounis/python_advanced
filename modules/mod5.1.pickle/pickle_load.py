from pickle import dumps, loads

d = [(1,3),{1,2},dumps]

serialized = dumps(d)
print(serialized)

deserialized = loads(serialized)
print(deserialized)