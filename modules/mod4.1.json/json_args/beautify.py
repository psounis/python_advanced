import json

a_person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25
}
with open("ob.json", "w") as f:
    json.dump(a_person, f, indent=2, sort_keys=True)